import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
import numpy as np
import cv2

import pimodule

INPUT_SIZE = (224, 224)  # Width, Height

class ImageProcessor:
    @staticmethod
    def preprocess_image(image):
        if isinstance(image, np.ndarray):
            if len(image.shape) == 3 and image.shape[2] == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)

        if not isinstance(image, Image.Image):
            raise ValueError("Input must be PIL Image or numpy array")

        if image.mode != 'RGB':
            image = image.convert('RGB')

        transform = transforms.Compose([
            transforms.Resize(INPUT_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                              std=[0.229, 0.224, 0.225])
        ])

        return transform(image)

class PicarXNet(nn.Module):
    def __init__(self):
        super(PicarXNet, self).__init__()
        # Input size: 3x224x224

        self.features = nn.Sequential(
            # Layer 1: 224x224x3 -> 110x110x24
            nn.Conv2d(3, 24, 5, stride=2, padding=0),
            nn.ReLU(),

            nn.Conv2d(24, 36, 5, stride=2, padding=0),
            nn.ReLU(),

            nn.Conv2d(36, 48, 5, stride=2, padding=0),
            nn.ReLU(),

            nn.Conv2d(48, 64, 3, padding=0),
            nn.ReLU(),

            nn.Conv2d(64, 64, 3, padding=0),
            nn.ReLU(),
        )

        self._to_linear = None
        self._calculate_flat_features(torch.zeros(1, 3, 224, 224))

        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(self._to_linear, 100),
            nn.ReLU(),
            nn.Linear(100, 50),
            nn.ReLU(),
            nn.Linear(50, 10),
            nn.ReLU(),
            nn.Linear(10, 3)  # [speed, direction, action]
        )

    def _calculate_flat_features(self, x):
        x = self.features(x)
        if self._to_linear is None:
            self._to_linear = x[0].shape[0] * x[0].shape[1] * x[0].shape[2]

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

class PicarXDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.samples = []
        self.processor = ImageProcessor()

        for label_file in os.listdir(os.path.join(data_dir, 'labels')):
            image_name = label_file.replace('.txt', '.jpg')
            if os.path.exists(os.path.join(data_dir, 'images', image_name)):
                self.samples.append((image_name, label_file))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        image_name, label_file = self.samples[idx]

        image_path = os.path.join(self.data_dir, 'images', image_name)
        image = Image.open(image_path)

        image_tensor = ImageProcessor.preprocess_image(image)

        label_path = os.path.join(self.data_dir, 'labels', label_file)
        with open(label_path, 'r') as f:
            data = f.read().strip().split(',')
            label = torch.tensor([float(x) for x in data], dtype=torch.float32)

        return image_tensor, label

def train_model(model, train_loader, criterion, optimizer, num_epochs=10, device='cuda'):
    model = model.to(device)
    model.train()

    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if i % 10 == 0:
                print(f'Epoch {epoch+1}, Batch {i}, Loss: {loss.item():.4f}')

        epoch_loss = running_loss / len(train_loader)
        print(f'Epoch {epoch+1} Complete, Average Loss: {epoch_loss:.4f}')

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    model = PicarXNet()

    dataset = PicarXDataset('training_data')
    train_loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("Starting training...")
    train_model(model, train_loader, criterion, optimizer, num_epochs=100, device=device)

    print("Saving model...")
    torch.save(model.state_dict(), 'picarx_model.pth')
    print("Model saved successfully!")

# if __name__ == '__main__':
#     main()


pimodule.init()

class PicarXInference:
    def __init__(self, model_path):
        # Set device
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f'Using device: {self.device}')
        
        # Load model
        self.model = PicarXNet()
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.to(self.device)
        self.model.eval()
        
    def process_image(self, image):
        """
        Process a single image and return predictions
        image can be: PIL Image, numpy array, or path to image file
        """
        # Handle different input types
        if isinstance(image, str):
            image = Image.open(image)
        elif isinstance(image, np.ndarray):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            
        # Preprocess image
        image_tensor = ImageProcessor.preprocess_image(image)
        image_tensor = image_tensor.unsqueeze(0)  # Add batch dimension
        image_tensor = image_tensor.to(self.device)
        
        # Get predictions
        with torch.inference_mode():
            output = self.model(image_tensor)
            speed, direction, action = output[0].cpu().numpy()
            
        return {
            'speed': float(speed),
            'direction': float(direction),
            'action': 'forward' if float(action) > 0.5 else 'backward'
        }

def main():
    # Example usage
    model_path = 'picarx_model.pth'
    inference = PicarXInference(model_path)
    
    # Test with a single image
    test_image_path = 'IMG_2712.jpg'  # Replace with your test image
    predictions = inference.process_image(test_image_path)
    
    print("\nPredictions:")
    print(f"Speed: {predictions['speed']:.2f}")
    print(f"Direction: {predictions['direction']:.2f}")
    print(f"Action: {predictions['action']}")
    

if __name__ == '__main__':
    main()

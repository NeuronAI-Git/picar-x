from picarx import Picarx
from vilib import Vilib
import time
import random

class HumanTrackingRobot:
    def __init__(self):
        # Initialize PiCar and Vision Library
        self.px = Picarx()
        
        # Camera and detection setup
        Vilib.camera_start()
        Vilib.display()
        Vilib.face_detect_switch(True)
        
        # Tracking parameters
        self.pan_angle = 0
        self.tilt_angle = 0
        
    def clamp_angle(self, angle, min_angle=-35, max_angle=35):
        """Clamp angle within specified range."""
        return max(min(angle, max_angle), min_angle)
    
    def scan_randomly(self):
        """Perform a random scanning movement to look around."""
        # Random pan movement
        pan_delta = random.uniform(-10, 10)
        self.pan_angle = self.clamp_angle(self.pan_angle + pan_delta)
        self.px.set_cam_pan_angle(self.pan_angle)
        
        # Random tilt movement
        tilt_delta = random.uniform(-10, 10)
        self.tilt_angle = self.clamp_angle(self.tilt_angle + tilt_delta)
        self.px.set_cam_tilt_angle(self.tilt_angle)
        
        # Rotation in place with small, varied angle
        rotation_speed = random.uniform(20, 40)
        rotation_direction = random.choice([-1, 1])
        self.px.set_dir_servo_angle(rotation_direction * 15)
        self.px.forward(rotation_speed)
        time.sleep(0.5)
        self.px.stop()
    
    def track_human(self):
        """Track a detected human with camera and body rotation."""
        coordinate_x = Vilib.detect_obj_parameter['human_x']
        coordinate_y = Vilib.detect_obj_parameter['human_y']
        
        # Camera pan tracking
        pan_adjust = (coordinate_x * 10 / 640) - 5
        self.pan_angle += pan_adjust
        self.pan_angle = self.clamp_angle(self.pan_angle)
        self.px.set_cam_pan_angle(self.pan_angle)
        
        # Camera tilt tracking
        tilt_adjust = -((coordinate_y * 10 / 480) - 5)
        self.tilt_angle += tilt_adjust
        self.tilt_angle = self.clamp_angle(self.tilt_angle)
        self.px.set_cam_tilt_angle(self.tilt_angle)
        
        # Body rotation tracking
        body_rotation = (coordinate_x * 30 / 640) - 15
        self.px.set_dir_servo_angle(body_rotation)
        
        # Slow rotation in place
        rotation_speed = 20
        self.px.forward(rotation_speed)
        time.sleep(0.1)
        self.px.stop()
    
    def run(self):
        """Main run method to control robot behavior."""
        try:
            while True:
                # Check for human detection
                if Vilib.detect_obj_parameter['human_n'] > 0:
                    # Human detected, track it
                    self.track_human()
                else:
                    # No human, perform random scanning
                    self.scan_randomly()
                
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("Stopping robot...")
        finally:
            self.px.stop()
            print("Robot stopped.")

def main():
    robot = HumanTrackingRobot()
    robot.run()

if __name__ == "__main__":
    main()

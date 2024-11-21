import pollinations
from robot_hat import TTS

model = pollinations.text(
  model=pollinations.text_default,
  contextual=True
)
tts = TTS()

def main():
    tts.lang("en-US")
    tts.say("wow thats cool bro")
    while True:
        response = model.generate(input(">>> ")).text
        print(response)
        tts.say(response)

if __name__ == "__main__":
    main()

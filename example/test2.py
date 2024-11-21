from robot_hat import TTS

tts = TTS()

def main():
    tts.lang("en-US")
    tts.say("wow thats cool bro")
    while True:
        tts.say(input(">>> "))

if __name__ == "__main__":
    main()

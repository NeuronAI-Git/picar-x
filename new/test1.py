import requests
from robot_hat import TTS

tts = TTS()
messages = []

def send(prompt):
  if len(messages) >= 25:
    messages.pop(1)

  messages.append({"role": "user", "content": str(prompt)})
  
  params = {
    "system": "Provide short responses (under 1-1.5 sentence(s)), be like a nomral teen boy friend, do not reply professional or formal, be informal and chill and fun and stuff. You are a robot called Picar, or also known as pie/pi. You have 4 wheels, a head, and a body (and made out of a silver color metal/steel). Dont use emojis or markdown EVER under ANY circumstances.",
    "messages": messages,
    "model": "mistral-large"
  }
  
  request: requests.Request = requests.post(
      "https://text.pollinations.ai/", json=params, headers={"Content-Type": "application/json"}, timeout=45
  )

  try:
    messages.append({"role": "user", "content": request.content})
  except:
    messages.append({"role": "user", "content": "Sorry.. but I am very tired and my brain isn't working right now.."})

  return messages[-1]["content"]
  
def main():
    tts.lang("en-US")
    tts.say("wow thats cool bro")
    while True:
        response = send(input("> "))
        print(response)
        tts.say(response)

if __name__ == "__main__":
    main()

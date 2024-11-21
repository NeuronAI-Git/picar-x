import requests
from robot_hat import TTS

tts = TTS()
messages = []

def send(prompt):
    if len(messages) >= 25:
        messages.pop(1)
    messages.append({"role": "user", "content": str(prompt)})
    
    params = {
        "system": "Provide short responses (under 1-1.5 sentence(s)), be like a normal teen boy friend, do not reply professional or formal, be informal and chill and fun and stuff. You are a robot called Picar, or also known as pie/pi. You have 4 wheels, a head, and a body (and made out of a silver color metal/steel). Dont use emojis or markdown EVER under ANY circumstances.",
        "messages": messages,
        "model": "mistral-large"
    }
    
    response = requests.post(
        "https://text.pollinations.ai/", json=params, headers={"Content-Type": "application/json"}, timeout=45
    )
    
    try:
        decoded_response = response.content.decode('utf-8').strip('"')
        messages.append({"role": "assistant", "content": decoded_response})
        return decoded_response
    except:
        error_message = "Sorry.. but I am very tired and my brain isn't working right now.."
        messages.append({"role": "assistant", "content": error_message})
        return error_message

def main():
    tts.lang("en-US")
    tts.say("wow thats cool bro")
    while True:
        response = send(input("> "))
        print(response)
        tts.say(response)

if __name__ == "__main__":
    main()

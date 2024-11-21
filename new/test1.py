import requests
from robot_hat import TTS

tts = TTS()
messages = []

messages.append({"role": "system", "content": "Provide short responses (under 1-1.5 sentence(s)), be like a nomral teen boy friend, do not reply professional or formal, be informal and chill and fun and stuff. You are a robot called Picar, or also known as pie/pi. You have 4 wheels, a head, and a body (and made out of a silver color metal/steel). Dont use emojis or markdown EVER under ANY circumstances."})

def send(prompt):
    if len(messages) >= 25:
        messages.pop(1)

    messages.append({"role": "user", "content": str(prompt)})

    params = {
        "messages": messages,
        "model": "mistral-large"
    }

    request = requests.post(
        "https://text.pollinations.ai/", json=params, headers={"Content-Type": "application/json"}, timeout=45
    )

    try:
        response_content = request.content
        messages.append({"role": "user", "content": response_content})
        return response_content
    except:
        messages.append({"role": "user", "content": "Sorry.. but I am very tired and my brain isn't working right now.."})
        return "Sorry.. but I am very tired and my brain isn't working right now.."

def main():
    tts.lang("en-US")
    while True:
        response = send(input("> "))
        try:
            decoded_response = response.decode('utf-8')
            escaped_response = decoded_response.replace("'", "\\'")
            print(escaped_response)
            tts.say(escaped_response)
        except Exception as e:
            print(f"Error processing response: {e}")


if __name__ == "__main__": main()
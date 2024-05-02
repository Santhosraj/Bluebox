from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

openrouter_data = {
    "provider": "openrouter",
    "apiKey": ""
}

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/make_call', methods=['POST'])
def make_call():
    url = "https://api.vapi.ai/call/phone"

    payload = {
        "maxDurationSeconds": 500,
        "assistantId": "cd2420bd-8449-4fc4-be70-ffc6e3e6bd8b",
        "assistant": {
            "transcriber": {
                "provider": "deepgram",
                "model": "nova-2",
                "language": "en-US"
            },
            "model": {
                "provider": "openrouter",
                "model": "gemini-pro",
                "messages": [
                    {
                        "content": "You are a world class customer service agent. You are a conversational assistant named Alice. Use short, conversational responses as if you're having a live conversation. Your response should be under 50 words. Do not respond with any code, only conversation. Do not say that you are an ai chatbot",
                        "role": "assistant"
                    }
                ]
            },
            "voice": {
                "provider": "deepgram",
                "voiceId": "luna"
            },
            "silenceTimeoutSeconds": 10,
            "responseDelaySeconds": 1,
            "llmRequestDelaySeconds": 1,
            "numWordsToInterruptAssistant": 1,
            "maxDurationSeconds": 500,
            "backgroundSound": "off",
            "name": "Alice",
            "firstMessage": "Hey , i am alice at your service , how's your day?",
            "endCallMessage": "Thanks for reaching , have a great day !",
            "endCallPhrases": ["bye", "Thankyou", "goodbye"],
            "endCallFunctionEnabled": True,
            "recordingEnabled": True
        },
        "customer": {
            "number": request.json['customer']['number'],
            "name": request.json['customer']['name']
        },
        "phoneNumberId": "3a2b425c-7f89-4b5b-b8f7-f4c30144f06e",
        "phoneNumber": {
            "twilioPhoneNumber": "+14242567980",
            "twilioAccountSid": "",
            "twilioAuthToken": ""
        }
    }

    headers = {
        "Authorization": "Bearer <>",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return "Call Initiated....."

if __name__ == '__main__':
    app.run(debug=True)

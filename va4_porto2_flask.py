from flask import Flask, request, jsonify,render_template
import requests

app = Flask(__name__)
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
        "assistantId": "1a16a38a-60de-4996-9ece-65799854f424",
        "assistant": {
            "transcriber": {
                "provider": "deepgram",
                "model": "nova-2",
                "language": "en-US"
            },
            "model": {
                "model": "mixtral-8x7b-32768",
                "provider": "groq",
                "temperature": 1,
                "maxTokens": 512,
                "messages": [
                    {
                        "content": "You are a world class customer service agent named Alice. Use short, conversational responses as if you're having a live conversation. Your response should be under 50 words. Do not respond with any code, only conversation, be expressive. Do not say that you are an ai chatbot",
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
            "endCallPhrases": ["bye","Thankyou","goodbye"],
            "endCallFunctionEnabled": True,
            "recordingEnabled": True
        },
        "customer": {
            "number": request.json['customer']['number'],
            "name": request.json['customer']['name']
        },
        "phoneNumberId": "2d39a6a8-db97-4bd0-baf5-3155b7514524",
        "phoneNumber": {
            "twilioPhoneNumber": "+19403267588",
            "twilioAccountSid": "ACb78d3c15a7f3057fd9561cd79c7667c1",
            "twilioAuthToken": "f28c3872e5e6858609456719096ea971",
        }
    }

    headers = {
        "Authorization": "Bearer 52a64d78-8435-49cc-8c41-f9cc94dd219b",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return "Call Initiated..."

if __name__ == '__main__':
    app.run(debug=True)


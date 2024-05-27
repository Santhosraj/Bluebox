# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:21:23 2024

@author: SanthosRaj
"""

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods = ["GET","POST"])
def voice():
    resp=VoiceResponse()
    resp.say("Hello San !Have fun")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
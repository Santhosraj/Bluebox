# -*- coding: utf-8 -*-

"""
Created on Thu Apr 11 11:03:12 2024
@author: SanthosRaj
"""

import os
import requests
from dotenv import load_dotenv
import subprocess
import shutil
import time
from deepgram import Deepgram

load_dotenv()
DG_API_KEY = os.getenv("DEEPGRAM_API_KEY")
MODEL_NAME = "aura-luna-en"

def is_installed(lib_name: str) -> bool:
    lib = shutil.which(lib_name)
    return lib is not None

def play_stream(audio_stream, use_ffmpeg=True):
    player = "ffplay"
    player_command = ['ffplay', '-autoexit', '-', '-nodisp']
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    for chunk in audio_stream:
        if chunk:
            player_process.stdin.write(chunk)
            player_process.stdin.flush()

    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()

def send_tts_request(text):
    DEEPGRAM_URL = "https://api.deepgram.com/v1/speak?model=aura-luna-en"
    headers = {
        "Authorization": f"Token {DG_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        
    }

    with requests.post(DEEPGRAM_URL, stream=True, headers=headers, json=payload) as r:
        play_stream(r.iter_content(chunk_size=1024))

text = "Hello there, thanks for calling, is there any issue?"
send_tts_request(text)

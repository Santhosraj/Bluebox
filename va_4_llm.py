# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:26:30 2024

@author: SanthosRaj
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

load_dotenv()

def batch():
    chat = ChatGroq(temprature = 0 , model_name= "mixtral-8x7b-32768", groq_api_key = os.getenv("GROQ_API_KEY"))
    system = "You are a Customer Support Representative at a product and service based company. Be resourceful and efficient."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system",system),("human",human)])
    chain = prompt|chat
    print(chain.invoke({"text":"I am having an issue with my wifi router"}))
    
def streaming():
    chat = ChatGroq(temperature = 0 , model_name = "mixtral-8x7b-32768", groq_api_key= os.getenv("GROQ_API_KEY"))
    prompt = ChatPromptTemplate.from_messages([("human","list 2 reasons on {topic}")])
    chain = prompt|chat
    for chunk in chain.stream({"topic":"Why my router is not working"}):
        print(chunk.content,end = "", flush = True)
        
streaming()
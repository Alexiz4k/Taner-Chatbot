import random
import json
import pickle
import numpy as np
import sys
import os
import time
from datetime import date
import pyttsx3

os.system("clear")

#comienza el engine del habla

engine = pyttsx3.init('espeak')

def talk(text):
    engine.say(text)
    engine.runAndWait()
#termina el engine del habla

#comienza el saludo principal segun la hora
hora = time.strftime("%H") #se obtiene la hora, el formato "%H" define que es de 24 horas

if int(hora) >= 0 and int(hora) <= 12 :
    talk("Bienvenido, Buenos dias")
    print("Bienvenido, Buenos dias")
if int(hora) >= 13 and int(hora) <= 17 :
    talk("Bienvenido, Buenas tardes")
    print("Bienvenido, Buenas tardes")
if int(hora) >= 18 and int(hora) <= 24 :
    talk("Bienvenido, Buenas noches")
    print("Bienvenido, Buenas noches")

#termina el saludo principal segun la hora

#comienza chatbot

import nltk
from nltk.chat.util import Chat, reflections

pairs = json.loads(open('pairs.json').read())
reflections = json.loads(open('reflections.json').read())

#resultados

def chat():
    print("Hi! I am a chatbot created by Analytics Vidhya for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()




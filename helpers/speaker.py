import pyttsx3
from random import choice

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

def speak(audio):
    if(type(audio) == list):
        engine.say(choice(audio))
    elif(type(audio) == str):
        engine.say(audio)
        
    engine.runAndWait()
import datetime
import webbrowser
import os
from time import strftime
import pyttsx3
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("good morning robbie")
    elif(hour>=12 and hour<=17):
        speak("good afternoon robbie")
    elif(hour>=17):
        speak("good evening robbie")
if (__name__=="__main__"): 
    wishme()
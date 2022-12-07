

import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from AppOpener import run
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty("voices", voices[0].id)


def speak(audio):
    """_summary_
    This function is to speak out whatever audio(string) we provide as input.
    Args:
        audio (_type_): _description_
        Here 'audio' is of str dtype.
    """
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    """_summary_
    This function is to wish the user at the begining of any operation. 
    It first checks the current time(hour var) and then the conditional follows.
    Every conditional statement here calls the speak(audio) function where audio is equal to the wish string.
    """
    hour = int(dt.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        
    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon")
        
    else:
        speak("Good Evening")
        

def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("recognising ...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User Said :- {query}\n")
        
        
    except Exception as e:
        # print(e)
        
        print("Say that again")
        return "None"
    return query


        
    
if __name__ == "__main__":
    wishme()
    speak("Hello! Vaibhav sir, I'm your personal assistant. Please tell me what I can do for you")
    
    """_summary_ 
    below we have created logic for various queries that the user will speak out. 
    """
    while True:

        query = takeCommands().lower()
        
        
        if 'wikipedia' in query:
            
            speak("Kindly wait for a while, let me search for the desired results from wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        if 'open youtube' in query:
            speak("Opening Youtube for you")
            webbrowser.open("youtube.com")
            
        if 'open hackerrank' in query:
            speak("Opening Hacker Rank for you, Happy coding")
            webbrowser.open("hackerrank.com")
            
        if 'open google' in query:
            speak("opening google for you")
            webbrowser.open("google.com")
            
        if 'open stackoverflow' in query:
            speak("opening stackoverflow for you, happy coding")
            webbrowser.open("stackoverflow.com")
            
        if 'play music' in query:
            speak("Opening Spotify for you")
            run("spotify")
            
        if 'open whatsapp' in query:
            speak("Opening whatsapp for you")
            run("whatsapp")
            
        if 'time' in query:
            t = dt.datetime.now().strftime('%H:%M')
            speak(f" the time right now is {t}")
            
            
        if "mail" in query:
            speak("opening gmail for you")
            webbrowser.open("gmail.com")
            
        if 'bye' in query:
            speak('bye')
            raise SystemExit
            
        
            
            
        
            
            
            
        
            
            
    
    
    
    
    


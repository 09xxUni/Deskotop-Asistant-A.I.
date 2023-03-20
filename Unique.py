import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import time
from tkinter import *


start=pyttsx3.init("sapi5")
voices=start.getProperty("voices")
start.setProperty('voice',voices[1].id)



def speak(audio):
    start.say(audio)
    start.runAndWait()


def takeRequest():
    request=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening to commands....")
        request.pause_threshold = 1;
        request.energy_threshold = 4000
        request.dynamic_energy_threshold = True   
        audio=request.listen(source)
    try:
        print("Processing.......")
        command=request.recognize_google(audio,language='en-in')
        print(f"You said {command}")
    except Exception as e: 
        print("Can't hear you!! say it loud")
        return "None"
    return command


def bydefault():

    speak("Hello Boss")

    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
        speak("How Can I help you")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        speak("How Can I help you")
    else:
        speak("Good Evening")
        speak("How Can I help you")


def function():
    execution=True
    while execution:
        command = takeRequest().lower()
        
        if 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open instagram' in command:
            webbrowser.open("instagram.com")

        elif 'who are you' in command:
            speak("My name is Emi")
            time.sleep(0.1)
            speak("I am an Artificial Intelligence created by Mister Unique")

        elif 'open vscode' in command:
            location="C:\\Users\\uniqu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\Programs\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(location)

        elif 'open eclipse' in command:
            location="C:\\Users\\uniqu\\OneDrive\\Desktop\\Eclipse IDE for Java Developers - 2022-12.lnk"
            #"C:\Users\uniqu\OneDrive\Desktop\Eclipse IDE for Java Developers - 2022-12.lnk"
            os.startfile(location)

        elif "chrome" in command:
            location="C:\Program Files\Google\Chrome\Application\chrome.exe"
            #"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(location)

        elif 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            response = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            print(response)
            speak(response)
        
        elif 'stop' in command:

            execution=False 
        
        elif 'spotify' in command:
            webbrowser.open("javatpoint.com")

        elif "can you play music for me" in command:
            speak("Yes I can play")
            speak("What type of music you like")
        elif "romantic" in command:
            webbrowser.open("https://www.youtube.com/live/nhpxbzHrcH8?feature=share")
        elif ("motivation" or "motivational") in command:
            webbrowser.open("https://youtu.be/Wvzw24sZfqc")
        elif "Ninety's Songs" in command:
            webbrowser.open("https://www.youtube.com/live/EWCBO7ZEgLY?feature=share")
def call():
    bydefault()
    function()

def gui():
    root=Tk()
    label=Label(root,text="My Personal Asistant",font=("comic sans ms",20,"bold"),fg="orange")
    label.pack()
    b=Button(root,text="Start",height=3,width=9,font=("comic sans ms",10,"bold"),fg="orange",command=call)
    b.pack()
    root.geometry("300x300")
    root.config(bg="light blue")
    root.title("My Asistant")
    root.mainloop()



if __name__=="__main__":
    gui()

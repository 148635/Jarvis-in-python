from ipaddress import ip_address
from multiprocessing.context import SpawnProcess
from sqlite3 import Timestamp
from tkinter.font import names
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import random
import cv2
import pywhatkit as kit
from requests import get
import webbrowser
import os 
import sys
import subprocess as sp
from pynput.mouse import Button, Controller
from pynput import keyboard
from pynput.keyboard import Key, Listener
import smtplib
USERNAME="vamshi"
BOTNAME="JARVIS"
import subprocess as sp
from PIL import Image, ImageGrab

pathsforapps= {
    'notepad': "C:\\Windows\\notepad.exe"
}
names={"ronaldo":"ramchandervelpula10@gmail.com"}
whtsapp={"jay":"+918106643963","varun":"+917993981819"}
opening_text = [
    "Cool, I'm on it vamshi.",
    "Okay vamshi, I'm working on it.",
    "Just a second vamshi.","Chill out bro! Recognizing..."
]
engine=pyttsx3.init('sapi5')
# Set Rate
#engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# recognizes speech and coverts to text
def speech_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(source,timeout=1,phrase_time_limit=5)
    data=""
    try:
        s1=random.choice(opening_text)
        print(s1)
        speak(s1)
        data=r.recognize_google(audio,language='en-in')
        print("you said,",data)
        speak("you said ")
        speak(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio,Say that again please...")
        speech_to_text()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "none"
    return data
# GREET
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")
if __name__ =="__main__" :
    current=Controller()
    while True:
        greet_user()
        data=speech_to_text().lower()
        if "open notepad" in data:
            path=speech_to_text().lower()
            os.startfile(pathsforapp[path])
        elif "IP address" in data:
            ip_add=get('https://api64.ipify.org?format=json').json()
            speak(f"your IP address is {ip_add['ip']}")
        elif ("open youtube" in data) or ("play in youtube" in data):
            webbrowser.open('www.youtube.com')
        elif ("open wynk" in data) or ("play imusic" in data):
            webbrowser.open('www.wynkmusic.com')
        elif("open gmail" in data) or ("open  my mails" in data):
            webbrowser.open('www.gmail.com')
        elif("open google" in data):
            speak("what should i search in google bro!")
            cm=speech_to_text().lower()
            webbrowser.open(f"{cm}")
        elif ("send message" in data) or ("open whatsapp" in data) or ("send a message" in data):
            speak("to whom should i deliver this message bro!")
            name3=speech_to_text().lower()
            if "jay" in name3:
                number=whtsapp["jay"]
            elif "varun" in name3:
                number=whtsapp["varun"]
            speak("what is the message?")
            msg=speech_to_text().lower()
            speak(f"what time should i deliver the message to {name3}")
            time=speech_to_text().lower()
            kit.sendwhatmsg(number,msg,time)
        elif "play song on youtube" in data:
            speak("which song should i play?")
            song=speech_to_text().lower()
            kit.playonyt(song)
        ##elif "take a screenshot" or "take screenshot" or "take a snapshot" or "take snapshot" or "take snap" or "take a snap" in data:
            ##snapshot=ImageGrab.grab()
            ##drive='D:\\'
            ##folder_name=r"snapshots "
            ##folder_time=datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            ##extension={"jpg":".jpg","png":".png","gif":".gif"}
            ##speak("which extension do you want me to use?")
            ##exten=speech_to_text().lower()
            ##if "jpg" in exten:
                ##exten="jpg"
            ##elif "png" in exten:
                ##exten="png"
            ##elif "gif" in exten:
               ## exten="gif"
            ##folder_save=drive+folder_name+folder_time+extension[exten]
            ##snapshot.save(folder_save)
            ##speak("Horay!,snapshot saved bro!")

        elif "send an email" in data:
            try:
                speak("what should i say?")
                mail=speech_to_text().lower()
                speak("to whom should i send?")
                name3=speech_to_text().lower()
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('vvelpula356@gmail.com','vamshivelpula356@')
                server.sendmail('vvelpula356@gmail.com',names[name3],mail)
                speak("Email has been sent")
                server.quit()
            except Exception as e:
                print(e)
                speak("sorry bro,something went wrong!")
        #elif "open command prompt" or "open cmd" or "open terminal" in data:
            #os.system('start cmd')
        elif "who are you" in data:
            speak("I am Jarvis")
        elif "how are you" in data:
            speak("I am great with you")
        elif "take a note" in data:
            speak("what should i write?")
            note=speech_to_text().lower()
            if(note!=None):
                f=open('notes.txt','a')
                timestamp =datetime.now().strftime("%H:%M:%S")
                f.write(timestamp+'\n')
                note=note+'\n\n'
                f.write(note)
                f.close()
                speak("Done taking note bro!")
        #elif "record" in data:
            #current.press("Win","Alt","r")
            #speak("say stop recording to stop,recording now")
        #elif "stop recording" in data:
            #current.press("Win","Alt","r")
            #speak("stpped and saved your recording bro!")
        #elif "open cam" or "open camera" in data:
            #sp.run('start microsoft.windows.camera:',shell=True)
        speak("do you want to talk to me about anything")
        talk=speech_to_text().lower()
        if "no thanks" or "exit" in talk:
            speak("ok bro,have a good day!")
            sys.exit()
        else:
            continue


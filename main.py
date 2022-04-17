import os
import playsound
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime

import hashlib

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename =  hashlib.md5(datetime.now().strftime("%m/%d/%Y, %H:%M:%S").encode('utf-8')).hexdigest() + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

if "Jarvis" in text:
    speak("Hey, what can I do for you?")
    command = get_audio()
    if ("bye" in command):
        speak("Bye my friend")
elif "what is your name" in text:
    speak("My name is Jarvis")
else:
    speak("I didn't hear you well")
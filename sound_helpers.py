from gtts import gTTS
import hashlib
from datetime import datetime
import playsound
import os
import speech_recognition as sr

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
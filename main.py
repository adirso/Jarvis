from sound_helpers import speak, get_audio

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
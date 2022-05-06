from sound_helpers import speak

def handle_command(command):
    if "turn on" in command:
        speak("Turn on what")
    else:
        speak("I don't understand")
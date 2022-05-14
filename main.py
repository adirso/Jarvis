from sound_helpers import speak, get_audio
from commands_handler import handle_command
from dotenv import dotenv_values

run = True
config = dotenv_values(".env")

speak("Starting process now")

while run:
    text = get_audio()

    if "Jarvis" in text:
        speak("Hey, what can I do for you?")
        command = get_audio()
        handle_command(command)

    if "goodbye" in text:
        speak("Bye my friend")
        run = False

speak("Going to sleep")
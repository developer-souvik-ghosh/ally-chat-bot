import speech_recognition as sr
import pywhatkit
import pyttsx3
from datetime import date

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            return command.lower().strip()
    except:
        return None


def run_alexa(command):
    if "play" in command:
        play_command = command
        pywhatkit.playonyt(play_command)
    elif "date" in command:
        current_date = date.today().strftime("%m %d %Y")
        play_voice("Current date is " + current_date)
    else:
        play_voice("Try Again")


def play_voice(text):
    print(">>>> ", text)
    engine.say(text)
    engine.runAndWait()

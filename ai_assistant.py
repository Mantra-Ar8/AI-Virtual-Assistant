import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()
engine.setProperty('rate', 150) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("There was an error with the recognition service.")
        return ""

def execute_command(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif 'search' in command:
        topic = command.replace('search', '').strip()
        speak(f"Searching {topic} on Wikipedia")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I didn't understand that command.")

speak("Hello! I am Jarvis, your virtual assistant.")
while True:
    command = take_command()
    execute_command(command)

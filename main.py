import os
import time
import requests
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime

# Initialize recognizer
r = sr.Recognizer()

# Voice output
def speak(text):
    print(f"[Jarvis]: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Voice input
def listen():
    with sr.Microphone() as source:
        print("[Listening...]")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            query = r.recognize_google(audio)
            print(f"[You]: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that.")
        except sr.RequestError:
            speak("Sorry, voice service is not available.")
    return ""

# Commands
def tell_time():
    now = datetime.now().strftime("%H:%M")
    speak(f"The current time is {now}")

def open_app(name):
    try:
        os.system(f"start {name}")
        speak(f"Opening {name}")
    except Exception:
        speak(f"Failed to open {name}")

def get_joke():
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        speak(res['setup'])
        time.sleep(2)
        speak(res['punchline'])
    except:
        speak("Couldn't fetch a joke right now.")

def search_wikipedia(query):
    try:
        res = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}").json()
        if 'extract' in res:
            speak(res['extract'])
        else:
            speak("I couldn't find anything about that.")
    except:
        speak("An error occurred while searching Wikipedia.")

def main():
    speak("Hello boss, what to do today?")
    while True:
        command = listen()
        if not command:
            continue

        if "time" in command:
            tell_time()
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_app(app_name)
        elif "joke" in command:
            get_joke()
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            search_wikipedia(topic)
        elif "stop" in command or "exit" in command:
            speak("Goodbye boss.")
            break
        else:
            speak("Sorry, I don't understand that command.")

if _name_ == "_main_":
    main()

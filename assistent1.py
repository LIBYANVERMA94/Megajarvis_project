
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import sys

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        return ""

speak("Jarvis activated")
sleep_mode = False

while True:
    command = listen_command()

    if command == "":
        continue

    # EXIT
    if "exit" in command or "stop forever" in command:
        speak("Goodbye sir")
        sys.exit()

    # SLEEP MODE
    if "sleep" in command:
        speak("Going to sleep")
        sleep_mode = True
        continue

    if "wake up" in command:
        speak("I am back sir")
        sleep_mode = False
        continue

    if sleep_mode:
        continue

    # TIME
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # DATE
    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}")

    # OPEN
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # SEARCH YOUTUBE
    elif "search" in command and "youtube" in command:
        query = command.replace("search", "").replace("youtube", "").strip()
        speak("Searching YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    # SEARCH GOOGLE
    elif "search" in command and "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        speak("Searching Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    else:
        speak("I did not understand")

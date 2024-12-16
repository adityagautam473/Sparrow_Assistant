import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# # import requests
# from google.cloud import speech
# import io import noisereduce as nr 
# import numpy as np

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
musicLibrary

def speak(text):
    """Function to convert text to speech."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Choose a different voice (0 for male, 1 for female)
    engine.setProperty('rate', 150)           # Adjust speaking speed
    engine.setProperty('volume', 1.0)
    engine.say(text) 
    engine.runAndWait()
    newsapi = "fecff602b0f1442da210bf9b25d0281a"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://www.flipkart.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        # print(f"Playing {Song}")
    # elif "news" in c.lower():
    #     r = requests.get("https://newsapi.org/v2/everything?q=Apple&from=2024-12-16&sortBy=popularity&apiKey=API_KEY")


    
    

if __name__ == "__main__":
    # Speak a greeting
    speak("Hi! I am Sparrow.")
    while True:
        # Listen for the wake word Sparrow!
        # obtain audio from the microphone

        r = sr.Recognizer()
        
        # recognise speech using sphinx
        print("recognizing...")
        try: 

            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)

            wakeup_word  = r.recognize_google(audio)
            if(wakeup_word.lower() == "sparrow"):
                speak("Yes, I'm here.")
                #Listen for command
                with sr.Microphone() as source:
                    speak("What can I do for you?")
                    audio = r.listen(source)
                    command  = r.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")

        except Exception as e:
            print("Error; {0}".format(e))



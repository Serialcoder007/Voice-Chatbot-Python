import datetime
import os
import random
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import os

bot = ChatBot('Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ChatterBotCorpusTrainer')


# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
#
# engine.setProperty('voices', voices[0].id)


def speak(something):
    engine.say(something)
    engine.runAndWait()


def printWithSpeek(msg):
    print(msg)

    speak(msg)


def cmd(str):
    os.system(str)


def speekInput():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('\rListening...')
        rec.pause_threshold = 0.7
        listen = rec.listen(mic, phrase_time_limit=5)
    try:
        print("\rRecognizing... ")
        query = str(rec.recognize_google(listen, language='en-in'))
        print(f"Query: {query}")
    except Exception as e:
        print("I was unable to recognize, please say again! ")
        return "try again"
    return query.lower()


def main():
    while True:
        output = speekInput()
        if output == "try again":
            continue
        if output == 'exit':
            speak("GoodBye")
            exit()
        if 'open' in output:
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                     ["google", "https://www.google.com"], ["gmail", "https://www.gmail.com"]]
            for site in sites:
                if f"Open {site[0]}".lower() in output.lower():
                    printWithSpeek(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])
        else:
            printWithSpeek(str(bot.get_response(output)))

try:
    main()
except Exception as e:
    printWithSpeek(e)

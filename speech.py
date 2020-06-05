import speech_recognition as sr
import pyttsx3
import  pyaudio
from time import ctime
import webbrowser
import time
import playsound
import random
from gtts import gTTS
import os

r = sr.Recognizer()
def audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            Genevieve_speak(voice_data)
        except sr.UnknownValueError:
            Genevieve_speak('sorry i didn\'t get that')
        except sr.RequestError:
            Genevieve_speak('sorry, my service is down')
        return voice_data

def name(voice_data):
    if 'what is your name' in voice_data:
        Genevieve_speak('my name is Genevieve')
    if 'what is the time' in voice_data:
        Genevieve_speak(ctime())
    if 'what time is it' in voice_data:
        Genevieve_speak(ctime())
    if 'search' in voice_data:
        search  = audio('what do you wanna search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Genevieve_speak('what I found for' + search)
    if 'location' in voice_data:
        location  = audio('what location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Genevieve_speak('what I found for' + location)
    if 'close' in voice_data:
        exit()
    if 'stop' in voice_data:
        exit()
    if 'exit' in voice_data:
        exit()
def Genevieve_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
Genevieve_speak('please, how can I help you')
while 1:
    voice_data = audio()
    name(voice_data)

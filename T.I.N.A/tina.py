#Arquivo principal

import argparse
import queue
import sys
import sounddevice as sd
import pyaudio
import os
import pyttsx3

import json

from vosk import Model, KaldiRecognizer

#sintese de fala

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[-1].id)



def speak(text):


    engine.say(text)
    engine.runAndWait()



model = Model('IA\Tina\T.I.N.A\modelo')  #definindo o modelo (o que vai interpretar a voz)

rec = KaldiRecognizer(model, 16000)      #definindo a frequencia de leitura

p = pyaudio.PyAudio() #definindo o pyaudio
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000) 
stream.start_stream()

while True:    #loop que realiza a leitura do audio
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        print(result)

        if result is not None:
            text = result["text"]

            print(text)
            speak(text)
    

# print(rec.FinalResult())


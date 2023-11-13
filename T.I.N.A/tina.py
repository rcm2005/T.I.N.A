#Arquivo principal

import argparse
import queue
import sys
import sounddevice as sd
import pyaudio
import os
import pyttsx3
import core

import json
    
from vosk import Model, KaldiRecognizer

#sintese de fala

engine = pyttsx3.init() #inicia o modelo de sintese de fala

voices = engine.getProperty('voices') #pega a propriedade voices do computador
engine.setProperty("voice", voices[-1].id) #configura a voz do modelo



def speak(text):


    engine.say(text)
    engine.runAndWait()

#reconhecimento de fala

model = Model('Tina\T.I.N.A\modelo')  #definindo o modelo (o que vai interpretar a voz)
# \OneDrive\Estudos\2S\IA
rec = KaldiRecognizer(model, 16000)      #definindo a frequencia de leitura

p = pyaudio.PyAudio() #definindo o pyaudio
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000) 
stream.start_stream()

 #loop que realiza a leitura do audio

while True:   
    data = stream.read(20000)
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

            if text == 'que horas são' or text == 'me diga as horas':
                speak(core.SystemInfo.get_time())
    

print(rec.FinalResult())


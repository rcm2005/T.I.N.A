#Arquivo principal

import argparse
import queue
import sys
import sounddevice as sd
import pyaudio
import vosk
import os

from vosk import Model, KaldiRecognizer



model = Model('T.I.N.A/modelo')  #definindo o modelo (o que vai interpretar a voz)
rec = KaldiRecognizer(model, 16000)      #definindo a frequencia de leitura

p = pyaudio.PyAudio() #definindo o pyaudio
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000) ()
stream.start_stream()

while True:    #loop que realiza a leitura do audio
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())





import json
import time

from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import speech_recognition as sr


npy_data = np.load("vocals.npy")

audio_samples = npy_data.astype(np.int32)

audio = AudioSegment(audio_samples.tobytes(), frame_rate=48000, sample_width=2, channels=2)

# Leer el archivo JSON
with open("resultado.json") as file:
    segmentos_silencio = json.load(file)

for segmento in segmentos_silencio:
    inicio = segmento["inicio"]
    fin = segmento["fin"]
    segmento_audio = audio[inicio:fin]
    play(segmento_audio)
    time.sleep(1)


recognizer = sr.Recognizer()


def transcribir_audio(segmento_audio):
    recognizer = sr.Recognizer()

    with sr.AudioFile(segmento_audio.export("temp.wav", format="wav")) as archivo_audio:
        audio = recognizer.record(archivo_audio)

        texto = recognizer.recognize_google(audio, language="es-ES")  # Utiliza el servicio de reconocimiento de voz de Google

    return texto
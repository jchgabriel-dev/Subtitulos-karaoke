import sys
from pydub import AudioSegment
import os
import speech_recognition as sr

def process_audio(filename, times_file):
    txtf = open("audios/the_audio.txt", "w+")

    myaudio = AudioSegment.from_wav(filename)

    with open(times_file) as f:
        lines = f.readlines()

    for line in lines:
        print(line)
        if line.startswith("Inicio:") and line.endswith("Fin:\n"):
            continue 
        else:
            line = line.replace("Inicio:", "").replace("Fin:", "")
            start_time, end_time = line.strip().split(",") 
            start_time = int(start_time)
            end_time = int(end_time)

            chunk = myaudio[start_time:end_time] 

            chunkName = './audios/chunked/' + "filename" + "_{0}_{1}.wav".format(start_time, end_time)
            print('i am exporting', chunkName)
            chunk.export(chunkName, format="wav")

            file = chunkName
            r = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio_listened = r.listen(source)

                try:
                    rec = r.recognize_google(audio_listened)
                    txtf.write(rec + "\n")

                except sr.UnknownValueError:
                    txtf.write("-\n")
                    print("i dont recognize your audio")

                except sr.RequestError as e:
                    txtf.write("-\n")
                    print("could not get results")

try:
    os.makedirs("audios/chunked")
except:
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Debe proporcionar el nombre del archivo de audio y el nombre del archivo de tiempos como argumentos.")
        sys.exit(1)

    audio_filename = sys.argv[1]
    times_filename = "audios/segmentos.txt"
    process_audio(audio_filename, times_filename)

import numpy as np
import torch as th
from demucs.audio import save_audio
from pydub import AudioSegment
from scipy.io.wavfile import write
from pydub.playback import play



npy_data = np.load("no_vocals.npy")

audio_samples = npy_data.astype(np.float32)

audio_segment = AudioSegment(audio_samples.tobytes(), frame_rate=44100, sample_width=2, channels=2)
audio_player = play(audio_segment)
audio_player.start()


import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# Ruta y nombre del archivo de audio WAV
audio_file = "testing.wav"

# Lee el archivo de audio utilizando pydub y conviértelo en un array de muestras utilizando numpy
audio = AudioSegment.from_file(audio_file)
audio_samples = np.array(audio.get_array_of_samples())

fs = audio.frame_rate
print(fs)

time = np.arange(len(audio_samples)) / fs
print(time)

audio_duration = len(audio_samples) / fs
print(audio_duration)


# Grafica la forma de onda del audio utilizando el tiempo en el eje x
plt.plot(time, audio_samples)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Forma de Onda del Audio')
plt.xlim([0, audio_duration])  # Define el rango del eje x
plt.show()




import numpy as np


npy_data = np.load("vocals.npy")

audio_samples = npy_data.astype(np.int32)



npy_data = np.load("vocals.npy")

audio_samples = npy_data.astype(np.int32)

audio = AudioSegment(audio_samples.tobytes(), frame_rate=48000, sample_width=2, channels=2)

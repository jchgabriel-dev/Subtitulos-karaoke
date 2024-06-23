import sys
import numpy as np
from pyAudioAnalysis import audioSegmentation
from pydub import AudioSegment
import matplotlib.pyplot as plt


def cargar_audio(archivo):
    audio = AudioSegment.from_wav(archivo)
    if audio.channels > 1:
        audio = audio.set_channels(1)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
    fs = audio.frame_rate
    return samples, fs


def normalizar_audio(samples):
    normalized_samples = samples / np.max(np.abs(samples))
    return normalized_samples


def detectar_segmentos_discurso(normalized_samples, fs, umbral_inicio, umbral_silencio):
    segments = audioSegmentation.silence_removal(normalized_samples, fs, umbral_inicio, umbral_silencio, smooth_window=1.0)
    return segments


def guardar_segmentos(segmentos, fs, archivo_salida):
    with open(archivo_salida, 'w') as file:
        for segment in segmentos:
            start = int(segment[0] * 1000)  # Convertir a milisegundos
            end = int(segment[1] * 1000)  # Convertir a milisegundos
            file.write(f"Inicio: {start}, Fin: {end}\n")
    print(f"Los segmentos de discurso se han guardado en el archivo '{archivo_salida}'")


def mostrar_segmentos(samples, segments, fs, figura_salida):
    plt.figure()
    plt.plot(samples)
    for segment in segments:
        start = int(segment[0] * fs)
        end = int(segment[1] * fs)
        plt.axvspan(start, end, color='r', alpha=0.3)

    plt.savefig(figura_salida)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python tu_programa.py archivo umbral_inicio umbral_silencio archivo_salida")
        sys.exit(1)

    archivo = sys.argv[1]
    umbral_inicio = 0.01
    umbral_silencio = 0.01
    archivo_salida = './audios/segmentos.txt'

    samples, fs = cargar_audio(archivo)
    normalized_samples = normalizar_audio(samples)
    segments = detectar_segmentos_discurso(normalized_samples, fs, umbral_inicio, umbral_silencio)

    guardar_segmentos(segments, fs, archivo_salida)
    mostrar_segmentos(samples, segments, fs, './audios/imagen.png')

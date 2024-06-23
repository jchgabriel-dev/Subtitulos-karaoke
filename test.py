import json

import numpy as np
import matplotlib.pyplot as plt
import wave

from pydub import AudioSegment


npy_data = np.load("vocals.npy")

audio_samples = npy_data.astype(np.int32)

audio = AudioSegment(audio_samples.tobytes(), frame_rate=48000, sample_width=2, channels=2)
audio_samples = np.array(audio.get_array_of_samples())


fs = audio.frame_rate
amount = audio.frame_count()
signal_wave = audio.raw_data


umbral_amplitud = -40
duracion_segmento = 10
inicio_silencio = 0
segmentos_silencio = []
sonido_iniciado = False

sonido_iniciado2 = False
umbral_amplitud2 = -30

output_file = "resultado.json"
segmentos_silencio_json = []
segmentos_unidos_json = []

segmentos = []
segmentos_unidos = []

tiempo = 0
minimun = 1000
minimun2 = 2000
tiempo_minimo_unir = 100
duracion_maxima_segmento = 5
segmentos_vuelta = []
segmentos_vuelta_json = []


with open(output_file, "w") as file:
    for i in range(0, len(audio), duracion_segmento):
        segmento = audio[i:i+duracion_segmento]
        amplitud_promedio = segmento.dBFS

        if amplitud_promedio > umbral_amplitud:
            if not sonido_iniciado:
                inicio_sonido = i
                sonido_iniciado = True

        else:
            if sonido_iniciado and tiempo >= minimun and amplitud_promedio <umbral_amplitud:
                fin_sonido = i   # Convierte a segundos
                segmentos_silencio.append((inicio_sonido, fin_sonido))
                segmentos_silencio_json.append({"inicio": inicio_sonido, "fin": fin_sonido})

                sonido_iniciado = False
                tiempo = 0

        if tiempo < minimun and sonido_iniciado:
            tiempo += 10

        timestamp = f"{i//60000:02d}:{(i//1000)%60:02d}:{i%1000:03d}"
        segmentos.append((timestamp, amplitud_promedio, sonido_iniciado))


    segmento_actual = segmentos_silencio[0]
    for i in range(1, len(segmentos_silencio)):
        inicio_actual, fin_actual = segmento_actual
        inicio_siguiente, fin_siguiente = segmentos_silencio[i]

        if inicio_siguiente - fin_actual <= tiempo_minimo_unir:
            segmento_actual = (inicio_actual, fin_siguiente)
        else:
            segmentos_unidos.append(segmento_actual)
            segmentos_unidos_json.append({"inicio": inicio_actual, "fin": fin_actual})
            segmento_actual = (inicio_siguiente, fin_siguiente)

    # Agregar el último segmento
    segmentos_unidos.append(segmento_actual)
    tiempo = 0
    start = True

    for segmento in segmentos_unidos:
        inicio_segmento, fin_segmento = segmento
        duracion_segmento_actual = (fin_segmento - inicio_segmento) / 1000

        if duracion_segmento_actual > duracion_maxima_segmento:
            print(inicio_segmento, fin_segmento)
            for i in range(inicio_segmento, fin_segmento, duracion_segmento):
                segmento = audio[i:i+duracion_segmento]
                amplitud_promedio2 = segmento.dBFS

                if amplitud_promedio2 > umbral_amplitud2 or i == inicio_segmento:
                    if not sonido_iniciado2:
                        print("inicio", i, amplitud_promedio2)
                        inicio_sonido = i
                        sonido_iniciado2 = True

                else:
                    if sonido_iniciado2 and tiempo >= minimun2 and amplitud_promedio2 < umbral_amplitud2:
                        print("final", i, amplitud_promedio2)
                        fin_sonido = i  # Convierte a segundos

                        segmentos_vuelta.append((inicio_sonido, fin_sonido))
                        segmentos_vuelta_json.append({"inicio": inicio_sonido, "fin": fin_sonido})

                        sonido_iniciado2 = False
                        tiempo = 0

                if tiempo < minimun2 and sonido_iniciado2:
                    tiempo += 10

                if i == fin_segmento-10 and sonido_iniciado2:
                    tiempo = 0
                    sonido_iniciado2 = False
                    print("final", fin_segmento, amplitud_promedio2)
                    segmentos_vuelta.append((inicio_sonido, fin_segmento))
                    segmentos_vuelta_json.append({"inicio": inicio_sonido, "fin": fin_sonido})


        else:
            segmentos_vuelta.append((inicio_segmento, fin_segmento))
            segmentos_vuelta_json.append({"inicio": inicio_segmento, "fin": fin_segmento})

    json.dump(segmentos_vuelta_json, file)



if sonido_iniciado:
    fin_silencio = len(audio) / 1000  # Convierte a segundos
    print(f"Silencio detectado de {inicio_silencio} a {fin_silencio} segundos")

with open("resultado.txt", "w") as file:
    for segmento in segmentos:
        line = f"{segmento[0]}, {segmento[1]}, {segmento[2]}\n"
        file.write(line)


duration = int(amount/fs)
time = np.linspace(0, duration, num=int(amount))
signal_array = np.frombuffer(signal_wave, dtype=np.int32)

plt.figure(figsize=(10, 4))
plt.plot(time, signal_array)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Forma de Onda del Audio')


for mark_time in segmentos_silencio:
    test1 = mark_time[0]/1000
    test2 = mark_time[1]/1000
    plt.axvline(x=test1, color='r', linestyle='--')
    plt.axvline(x=test2, color='r', linestyle='--')

for mark_time in segmentos_unidos:
    test1 = mark_time[0]/1000
    test2 = mark_time[1]/1000
    plt.axvline(x=test1, color='b', linestyle='--')
    plt.axvline(x=test2, color='b', linestyle='--')

for mark_time in segmentos_vuelta:

    test1 = mark_time[0]/1000
    test2 = mark_time[1]/1000

    plt.axvline(x=test1, color='m', linestyle=':')
    plt.axvline(x=test2, color='m', linestyle=':')

plt.grid()
plt.show()


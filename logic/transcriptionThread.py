import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from pydub import AudioSegment
import matplotlib.pyplot as plt
import speech_recognition as sr


class TranscriptionThread(QThread):
    progress_updated = pyqtSignal(int)
    finished_updated = pyqtSignal()

    def __init__(self, video_data):
        super().__init__()
        self.video_data = video_data
        self.duracion_segmento = 10
        self.umbral_amplitud = -40
        self.deteccion_iniciada = False
        self.duracion_minima = 1000
        self.longitud_registrada = 0
        self.distancia_minima = 100

        self.inicio_segmento = 0
        self.fin_segmento = 0

        self.segmentos_general = []
        self.segmentos_unidos = []
        self.trasncription = []


    def run(self):
        self.segment_process()

    def segment_process(self):
        npy_data = np.load("vocals.npy")
        audio_samples = npy_data.astype(np.int32)
        audio = AudioSegment(audio_samples.tobytes(), frame_rate=48000, sample_width=2, channels=2)

        self.divide_segments(audio)
        self.progress_callback(30)
        self.join_segments()
        self.progress_callback(60)
        self.join_segments()

        for seg in self.segmentos_unidos:
            inicio = seg[0]
            fin = seg[1]
            segmento_audio = audio[inicio:fin]
            texto_transcrito = self.trasncription_audio(segmento_audio)
            if texto_transcrito is not None:
                self.trasncription.append({"inicio": inicio, "fin": fin, "texto": texto_transcrito})

        self.finished_updated.emit()
        self.video_data.add_transcription(self.trasncription)


    def divide_segments(self, audio):
        for i in range(0, len(audio), self.duracion_segmento):
            segmento = audio[i:i + self.duracion_segmento]
            amplitud = segmento.dBFS

            if amplitud > self.umbral_amplitud:
                if not self.deteccion_iniciada:
                    self.inicio_segmento = i
                    self.deteccion_iniciada = True
            else:
                if self.deteccion_iniciada and self.longitud_registrada >= self.duracion_minima and amplitud < self.umbral_amplitud:
                    self.fin_segmento = i
                    self.segmentos_general.append((self.inicio_segmento, self.fin_segmento))

                    self.deteccion_iniciada = False
                    self.longitud_registrada = 0

            if self.longitud_registrada < self.duracion_minima and self.deteccion_iniciada:
                self.longitud_registrada += 10

    def join_segments(self):
        segmento_actual = self.segmentos_general[0]

        for i in range(1, len(self.segmentos_general)):
            inicio_actual, fin_actual = segmento_actual
            inicio_siguiente, fin_siguiente = self.segmentos_general[i]

            if inicio_siguiente - fin_actual <= self.distancia_minima:
                segmento_actual = (inicio_actual, fin_siguiente)
            else:
                self.segmentos_unidos.append(segmento_actual)
                segmento_actual = (inicio_siguiente, fin_siguiente)

    def progress_callback(self, data):
        progress = data
        self.progress_updated.emit(progress)

    def trasncription_audio(self, segment):
        recognizer = sr.Recognizer()
        segment.export("temp.wav", format="wav")
        with sr.AudioFile("temp.wav") as archivo_audio:

            try:
                audio = recognizer.record(archivo_audio)
                texto = recognizer.recognize_google(audio, language="es-ES")
                return texto
            except:
                pass

        return None


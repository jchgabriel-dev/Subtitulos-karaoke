import math
import tempfile
import threading
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QWidget
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from pydub.playback import play

from data.videoData import VideoData
import numpy as np
import torch as th
import torchaudio
from demucs.api import Separator

from general.styleLoad import StyleLoad
from interface.separation import Separation
from interface.toolbar import Toolbar
from logic.separationLogic import SeparationLogic
from logic.settingsLogic import SettingsLogic
from logic.transcriptionLogic import TranscriptionLogic
from logic.separationThread import SeparationThread
from logic.transcriptionThread import TranscriptionThread


class ToolbarLogic(QWidget, StyleLoad):
    def __init__(self):
        super().__init__()
        self.toolbarInterface = Toolbar(self)
        self.video_data = VideoData()
        self.separation_thread = SeparationThread(self.video_data)
        self.transcription_thread = TranscriptionThread(self.video_data)

        self.separate_window = SeparationLogic(self.separation_thread)
        self.separation_thread.progress_updated.connect(self.separate_window.update_progress)
        self.separation_thread.finished_updated.connect(self.separate_window.finished_progress)

        self.transcription_window = TranscriptionLogic(self.separation_thread)
        self.transcription_thread.progress_updated.connect(self.transcription_window.update_progress)
        self.transcription_thread.finished_updated.connect(self.transcription_window.finished_progress)
        self.transcription_thread.finished_updated.connect(self.video_data.update_table)

        self.settings_window = SettingsLogic()

        self.button_new = self.toolbarInterface.create_button("Nuevo", "interface/icons/new.png", self.open_video)
        self.button_open = self.toolbarInterface.create_button("Abrir", "interface/icons/open.png", self.open_video)
        self.button_save = self.toolbarInterface.create_button("Guardar", "interface/icons/save.png", self.open_video)
        self.button_separate = self.toolbarInterface.create_button("Separar", "interface/icons/separate.png", self.separate_audio)
        self.button_lyric = self.toolbarInterface.create_button("Letra", "interface/icons/lyrics.png", self.transcription_audio)
        self.button_settings = self.toolbarInterface.create_button("Ajustes", "interface/icons/settings.png", self.settings_options)

        self.setLayout(self.toolbarInterface.create_layout(self.button_new, self.button_open, self.button_save, self.button_separate, self.button_lyric, self.button_settings))

    def open_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        title = "Abrir archivo de video"
        filters = "Archivos de Video (*.mp4 *.avi *.mkv);;Todos los archivos (*)"
        file_path, _ = QFileDialog.getOpenFileName(None, title, "",filters, options=options)

        if file_path:
            video_clip = VideoFileClip(file_path)
            video_clip = video_clip.set_fps(60)
            audio_segment = AudioSegment.from_file(file_path)

            self.video_data.add_video_clip(video_clip)
            self.video_data.add_audio_clip(audio_segment)

    def separate_audio(self):
        self.separate_window.show()
        self.separation_thread.start()

    def transcription_audio(self):
        self.transcription_window.show()
        self.transcription_thread.start()

    def settings_options(self):
        self.settings_window.show()








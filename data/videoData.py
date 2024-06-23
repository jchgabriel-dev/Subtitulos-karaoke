from PyQt5.QtWidgets import QLabel
from moviepy.video.VideoClip import TextClip

from logic.lineLogic import LineLogic


class VideoData:
    _instance = None

    def __init__(self):
        self.file_path = None
        self.video_clips = []
        self.audio_clips = []
        self.transcription = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VideoData, cls).__new__(cls)
            cls.video_screen = None
            cls.table_transcription = None

        return cls._instance

    def add_video_screen(self, video_screen):
        self.video_screen = video_screen

    def add_video_clip(self, video_clip):
        self.video_clips.append({"clip": video_clip, "inicio": 0, "fin": video_clip.duration})
        self.video_screen.update()

    def add_audio_clip(self, audio_clip):
        self.audio_clips.append(audio_clip)


    def update_table(self):
        self.table_transcription.update_table()

        for line in self.transcription:
            clip_texto = TextClip(line["texto"], fontsize=30, color='white', font='Arial-Bold')
            clip_texto = clip_texto.set_duration((line["fin"] - line["inicio"])/1000)
            clip_texto = clip_texto.set_start(line["inicio"]/1000)
            self.video_clips.append({"clip": clip_texto, "inicio": line["inicio"], "fin": line["fin"]})

        self.video_screen.update()

    def add_table_transcription(self, table_transcription):
        self.table_transcription = table_transcription

    def add_transcription(self, transcription):
        self.transcription = transcription[:]



import datetime
import math
import threading

import cv2
import pygame
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QWidget
from moviepy.video.VideoClip import TextClip, VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from pydub.playback import play

from data.timerData import TimerData
from data.videoData import VideoData
from general.styleLoad import StyleLoad
from interface.video import Video
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


class VideoLogic(QWidget, StyleLoad):
    def __init__(self):
        super().__init__()
        self.videoInterface = Video(self)
        self.timer_data = TimerData()
        self.video_data = VideoData()
        self.video_clips = self.video_data.video_clips
        self.audio_clips = self.video_data.audio_clips

        self.video_data.add_video_screen(self)
        self.back_button = self.videoInterface.create_button("interface/icons/back.png", self.skip_time_back)
        self.play_button = self.videoInterface.create_button("interface/icons/play.png", self.play_pause)
        self.next_button = self.videoInterface.create_button("interface/icons/next.png", self.skip_time_next)
        self.audio_combobox = self.videoInterface.create_combobox()
        self.audio_label = self.videoInterface.create_label()
        self.background = self.videoInterface.create_background()
        self.screen = self.videoInterface.create_screen(self.background)
        self.setLayout(self.videoInterface.create_layout(self.back_button, self.play_button, self.next_button, self.audio_combobox, self.audio_label, self.screen, self.background))

        self.clock = QTime()
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_frame)

        self.desired_fps = 60.0

        pygame.mixer.init()
        self.final_video = VideoClip()
        self.final_audio = None
        self.updatet = 0

    def update(self):
        self.updatet += 1
        print(self.updatet)
        clips = [video["clip"] for video in self.video_data.video_clips]
        self.final_video = CompositeVideoClip(clips)

    def play_pause(self):
        if not self.timer_data.is_running:
            self.timer_data.start()
            self.timer.start()
        else:
            self.timer.stop()
            self.timer_data.stop()


    def show_frame(self):
        elapsed_time = self.timer_data.time / 1000
        frame = self.final_video.get_frame(elapsed_time)

        width, height = self.get_size(frame)

        resized_frame = cv2.resize(frame, (width, height))

        qimage = QImage(resized_frame.data, resized_frame.shape[1], resized_frame.shape[0], resized_frame.strides[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.screen.setPixmap(pixmap)

    def get_size(self, frame):
        background_height = self.background.height() * 0.9
        background_width = self.background.width() * 0.9

        scale_factor = min(background_width / frame.shape[1], background_height / frame.shape[0])
        new_width = int(frame.shape[1] * scale_factor)
        new_height = int(frame.shape[0] * scale_factor)

        return new_width, new_height

    def skip_time_back(self):
        self.clock.addSecs(5)

    def skip_time_next(self):
        self.clock.addSecs(5)
        print(self.clock.elapsed() / 1000.0)

    def state_media(self, state):
        play_button = self.video_control.play_button

        if state == QMediaPlayer.PlayingState:
            play_button.setIcon(QIcon("interface/icons/pause.png"))
        elif state == QMediaPlayer.PausedState:
            play_button.setIcon(QIcon("interface/icons/play.png"))
        else:
            print(state)

    def set_duration(self, duration):
        duration_sec = int(duration / 1000)
        end_time = str(datetime.timedelta(seconds=duration_sec))
        self.video_time.end_time.setText(end_time)
        self.video_time.slider.setRange(0, duration)

    """
    def set_actual(self, duration):
        duration_sec = int(duration / 1000)
        act_time = str(datetime.timedelta(seconds=duration_sec))

        self.video_time.start_time.setText(act_time)
        self.video_time.slider.setValue(duration)

    def slider_event(self, event):
        slider = self.video_time.slider
        position = event.pos().x()
        max_value = slider.maximum()
        new_value = int((position / slider.width()) * max_value)
        slider.setValue(new_value)
        slider.setProperty("state", "active")
        slider.style().polish(slider)
        self.video_screen.mediaPlayer.setPosition(new_value)

    def slider_release(self, event):
        mediaPlayer = self.video_screen.mediaPlayer

        slider = self.video_time.slider
        slider.setProperty("state", "inactive")
        slider.style().polish(slider)

        if mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.video_screen.mediaPlayer.play()
        else:
            self.video_screen.mediaPlayer.pause()
        
    """



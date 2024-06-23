
from PyQt5.QtCore import QThread, pyqtSignal
from demucs.api import Separator
import numpy as np
import torch as th
import math


class SeparationThread(QThread):
    progress_updated = pyqtSignal(int)
    finished_updated = pyqtSignal()

    def __init__(self, video_data):
        super().__init__()
        self.video_data = video_data

    def run(self):
        self.separate_process()

    def stop(self):
        return

    def separate_process(self):
        separator = Separator(model="htdemucs", progress=True, callback=self.progress_callback)
        waveform = self.get_waveform()

        origin, res = separator.separate_tensor(waveform)
        no_vocals = th.zeros_like(waveform)
        source_to_exclude = "vocals"

        for source_name, source_waveform in res.items():
            if source_name != source_to_exclude:
                no_vocals += source_waveform

        np.save("no_vocals.npy", no_vocals.numpy())
        np.save("vocals.npy", res.get("vocals").numpy())

        self.finished_updated.emit()

    def progress_callback(self, data):
        progress = math.floor((data['segment_offset'] / data['audio_length']) * 100)
        self.progress_updated.emit(progress)

    def get_waveform(self):
        audio_segment = self.video_data.audio_clips[0]

        left_channel = audio_segment.split_to_mono()[0]
        right_channel = audio_segment.split_to_mono()[1]
        left_channel_np = np.array(left_channel.get_array_of_samples(), dtype=np.float32)
        right_channel_np = np.array(right_channel.get_array_of_samples(), dtype=np.float32)
        audio_np = np.vstack((left_channel_np, right_channel_np))
        waveform = th.from_numpy(audio_np)

        return waveform

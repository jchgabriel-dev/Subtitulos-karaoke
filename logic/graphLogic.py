import math
import threading

from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from data.timerData import TimerData
from data.videoData import VideoData
from general.styleLoad import StyleLoad
from interface.graph import Graph
from logic.itemLogic import ItemLogic
from logic.markerLogic import MarkerLogic

class GraphLogic(QWidget, StyleLoad):

    def __init__(self):
        super().__init__()
        self.graphInterface = Graph(self)

        self.width_sector = 100
        self.initial_time = 20.0
        self.division_number = 20

        self.total = self.initial_time * 60 * 1000

        self.zoom_factor = 1
        self.zoom_amount = 0.2

        self.timeline = self.graphInterface.create_timeline(self.paintEventTimeline, self.wheelEventTimeline)
        self.scrollHorizontal = self.graphInterface.create_scroll()

        self.time_marker = MarkerLogic(self.timeline)

        self.background_color = QColor(196, 196, 196)
        self.line_color = QColor(113, 113, 113)
        self.text_color = QColor(39, 39, 39)
        self.text_font = QFont("Helvetica", 8, 80)

        self.setLayout(self.graphInterface.create_layout(self.timeline, self.scrollHorizontal, self.time_marker))

        self.timerData = TimerData()
        self.timerData.add_observer(self)

    def wheelEventTimeline(self, event):
        delta = event.angleDelta().y() / 120
        self.zoom_factor += delta * self.zoom_amount
        self.zoom_factor = max(1.0, min(6.0, self.zoom_factor))
        self.timeline.update()

    def update_time(self, time):
        sector_time = self.initial_time / self.division_number
        ms = int(sector_time / 1000 / self.width_sector)
        print(ms)
        length_per_ms = self.total / self.division_number / 1000
        self.time_marker.setPosition(int(time * length_per_ms / 10000))


    def paintEventTimeline(self, event):
        painter = QPainter(self.timeline)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.text_font)
        painter.fillRect(0, 0, self.height(), self.width(), self.background_color)

        divisions = math.floor(self.division_number * self.zoom_factor)
        interval_duration = math.floor(self.initial_time * 60 / divisions)

        for time in range(0, divisions):
            initial = time * self.width_sector
            half = initial + math.floor(self.width_sector / 2)

            painter.setPen(QPen(self.line_color, 1))
            painter.drawLine(initial, 0, initial, self.height())
            painter.drawLine(half, 0, half, 10)

            painter.setPen(QPen(self.text_color))
            start_time = time * interval_duration
            time_string = f"{(start_time // 60):02d}:{(start_time % 60):02d}"
            painter.drawText(initial + 5, 15, time_string)

        self.timeline.setMinimumWidth(divisions * self.width_sector)

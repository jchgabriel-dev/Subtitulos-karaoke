import math

from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtWidgets import QWidget


class ItemLogic(QWidget):

    def __init__(self, timeline, width):
        super().__init__()
        self.time = 230
        self.timeline = timeline
        self.time = width
        self.background_color = QColor(255, 0, 0)
        self.line_color = QColor(113, 113, 113)
        self.text_color = QColor(39, 39, 39)
        self.text_font = QFont("Helvetica", 8, 80)
        self.paintEvent = self.paintEventItem


    def paintEventItem(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.text_font)

        top = math.floor(self.timeline.height() * 0.2)
        button = math.floor(self.timeline.height() * 0.6)

        painter.fillRect(0, top, self.timeline.width(), button, self.background_color)

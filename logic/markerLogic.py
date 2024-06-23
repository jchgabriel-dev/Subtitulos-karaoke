from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget


class MarkerLogic(QWidget):
    def __init__(self, timeline):
        super().__init__(timeline)
        self.timeline = timeline
        self.marker_color = QColor(0, 0, 0)
        self.marker_position = 0

    def setPosition(self, position):
        self.marker_position = position
        self.timeline.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.marker_position, 0, 2, self.timeline.height(), self.marker_color)
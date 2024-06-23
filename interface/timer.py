from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QLabel, QVBoxLayout


class Timer:
    def __init__(self, timer):
        super().__init__()
        timer.setAttribute(Qt.WA_StyledBackground, True)
        timer.cargar_css("style/timerStyle.css")
        timer.setObjectName("timer_style")

    def create_label(self):
        label = QLabel()
        label.setObjectName("seconds_style")
        label.setText("00:00:00.000")
        return label

    def create_layout(self, seconds):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(seconds)
        return layout
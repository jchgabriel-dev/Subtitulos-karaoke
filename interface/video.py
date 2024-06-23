from datetime import datetime
import datetime
from datetime import datetime

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSlider, QVBoxLayout, QComboBox

from general.styleLoad import StyleLoad


class Video:
    def __init__(self, video):
        super().__init__()
        video.setAttribute(Qt.WA_StyledBackground, True)
        video.cargar_css("style/videoStyle.css")
        video.setObjectName("video_style")
        video.setFixedHeight(350)

    def create_button(self, icon_path, function):
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(20, 15))
        button.setFixedSize(QSize(60, 20))
        button.setObjectName("button_style")
        button.clicked.connect(function)
        return button

    def create_label(self):
        label = QLabel()
        label.setText("Audios disponibles: ")
        label.setFixedWidth(150)
        label.setObjectName("option_style")
        return label

    def create_combobox(self):
        combo = QComboBox()
        combo.addItems(["Audio 1", "Audio 2", "Audio 3"])
        combo.setObjectName("combo_style")
        return combo

    def create_screen(self, background):
        screen = QLabel()
        return screen

    def create_background(self):
        background = QWidget()
        background.setAttribute(Qt.WA_StyledBackground, True)
        background.setObjectName("screen_style")
        return background

    def create_layout(self, back, play, next, combo, label, screen, background):
        mainLayout = QVBoxLayout()
        controlLayout = QHBoxLayout()
        audioLayout = QHBoxLayout()
        screenLayout = QVBoxLayout()

        controlLayout.setAlignment(Qt.AlignHCenter)
        controlLayout.addWidget(back)
        controlLayout.addWidget(play)
        controlLayout.addWidget(next)

        audioLayout.addWidget(label)
        audioLayout.addWidget(combo)

        screenLayout.setAlignment(Qt.AlignCenter)
        screenLayout.addWidget(screen)
        background.setLayout(screenLayout)

        mainLayout.addLayout(audioLayout)
        mainLayout.addWidget(background)
        mainLayout.addLayout(controlLayout)

        return mainLayout


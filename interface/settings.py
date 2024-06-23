from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout


class Settings:
    def __init__(self, settings):
        settings.cargar_css("style/settingsStyle.css")
        settings.setWindowTitle("Separacion de audio")
        settings.setGeometry(100, 100, 400, 120)


    def create_window(self):
        main = QWidget()
        main.setObjectName("settings_style")
        main.setAttribute(Qt.WA_StyledBackground, True)
        return main

    def create_layout(self, label_segmento, label_amplitud, text_segmento, text_amplitud, button_cancel, button_save):
        layoutMain = QVBoxLayout()
        layoutSegmento = QHBoxLayout()
        layoutAmplitud = QHBoxLayout()
        layoutButton = QHBoxLayout()

        layoutSegmento.addWidget(label_segmento)
        layoutSegmento.addWidget(text_segmento)

        layoutAmplitud.addWidget(label_amplitud)
        layoutAmplitud.addWidget(text_amplitud)

        layoutButton.addWidget(button_cancel)
        layoutButton.addWidget(button_save)

        layoutMain.addLayout(layoutSegmento)
        layoutMain.addLayout(layoutAmplitud)
        layoutMain.addLayout(layoutButton)

        return layoutMain


    def create_text(self):
        text = QLineEdit()
        text.setObjectName("text_line")
        return text

    def create_button(self, text, function):
        button = QPushButton()
        button.setText(text)
        button.setFixedSize(QSize(100, 25))
        button.setObjectName("button_style")
        button.clicked.connect(function)
        return button

    def create_label(self, text):
        label = QLabel()
        label.setText(text)
        label.setObjectName("label_style")
        return label
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from general.styleLoad import StyleLoad
class Separation(StyleLoad):
    def __init__(self, progress):
        super().__init__()
        progress.cargar_css("style/separationStyle.css")
        progress.setWindowTitle("Separacion de audio")
        progress.setGeometry(100, 100, 400, 120)


    def create_window(self):
        main = QWidget()
        main.setObjectName("progress_style")
        main.setAttribute(Qt.WA_StyledBackground, True)
        return main

    def create_layout(self, percentage_label, progress_bar, cancel_button):
        layoutMain = QVBoxLayout()
        layoutBar = QVBoxLayout()
        layoutBar.addWidget(percentage_label)
        layoutBar.addWidget(progress_bar)
        layoutBar.setSpacing(10)

        layoutBut = QHBoxLayout()
        layoutBut.addWidget(cancel_button)
        layoutBut.setAlignment(Qt.AlignRight)

        layoutMain.addLayout(layoutBar)
        layoutMain.addLayout(layoutBut)
        layoutMain.setAlignment(Qt.AlignCenter)

        return layoutMain
    def create_button(self, function):
        button = QPushButton()
        button.setText("Cerrar")
        button.setFixedSize(QSize(100, 25))
        button.setObjectName("button_style")
        button.clicked.connect(function)
        button.setEnabled(False)
        return button

    def create_progress_bar(self):
        bar = QProgressBar()
        bar.setGeometry(10, 50, 380, 30)
        bar.setTextVisible(False)
        bar.setObjectName("progress_bar")
        return bar

    def create_label(self, progress):
        label = QLabel()
        label.setText(f"Progreso: {progress} %")
        label.setObjectName("label_style")
        return label





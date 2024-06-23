import os
import sys

import appdirs
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QHBoxLayout

from data.timerData import TimerData
from data.videoData import VideoData
from general.styleLoad import StyleLoad
from logic.graphLogic import GraphLogic
from logic.tableLogic import TableLogic
from logic.timerLogic import TimerLogic
from logic.toolbarLogic import ToolbarLogic
from logic.videoLogic import VideoLogic
from table import Table
from toolbar import Toolbar


class MainWindow(QMainWindow, StyleLoad):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("APLICATIVO KARAOKE")
        self.setGeometry(100, 100, 800, 600)
        self.create_ubication()

        toolbar = ToolbarLogic()
        table = TableLogic()
        video = VideoLogic()
        timer = TimerLogic()
        graph = GraphLogic()

        hLayout = QHBoxLayout()
        hLayout.setAlignment(Qt.AlignLeft)
        hLayout.addWidget(table)
        hLayout.addWidget(video)
        hLayout.setStretch(0, 3)
        hLayout.setStretch(1, 4)

        gLayout = QHBoxLayout()
        gLayout.setAlignment(Qt.AlignLeft)
        gLayout.addWidget(timer)
        gLayout.addWidget(graph)
        gLayout.setStretch(0, 1)
        gLayout.setStretch(1, 4)

        vLayout = QVBoxLayout()
        vLayout.setAlignment(Qt.AlignTop)
        vLayout.addWidget(toolbar)
        vLayout.addLayout(hLayout)
        vLayout.addLayout(gLayout)

        mainWidget = QWidget()
        mainWidget.setLayout(vLayout)
        self.setCentralWidget(mainWidget)

    def create_ubication(self):
        app_data_dir = appdirs.user_data_dir(appname="Aplicativo Karaoke")
        os.makedirs(app_data_dir, exist_ok=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

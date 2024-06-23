from PyQt5.QtWidgets import QMainWindow

from general.styleLoad import StyleLoad
from interface.separation import Separation
from interface.transcription import Transcription


class TranscriptionLogic(QMainWindow, StyleLoad):

    def __init__(self, transcription_thread):
        super().__init__()
        self.progress = 0
        self.transcription_thread = transcription_thread
        self.progressInterface = Transcription(self)

        self.percentage_label = self.progressInterface.create_label(self.progress)
        self.progress_bar = self.progressInterface.create_progress_bar()
        self.cancel_button = self.progressInterface.create_button(self.cancel_execution)

        self.mainWidget = self.progressInterface.create_window()
        self.mainWidget.setLayout(self.progressInterface.create_layout(self.percentage_label, self.progress_bar, self.cancel_button))
        self.setCentralWidget(self.mainWidget)

    def update_progress(self, progress):
        self.progress = progress
        self.progress_bar.setValue(self.progress)
        self.percentage_label.setText(f"Progreso: {self.progress} %")

    def finished_progress(self):
        self.progress = 100
        self.progress_bar.setValue(self.progress)
        self.percentage_label.setText(f"Completado: {self.progress} %")
        self.cancel_button.setEnabled(True)

    def cancel_execution(self):
        self.close()
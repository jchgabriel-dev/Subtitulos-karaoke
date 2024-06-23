from PyQt5.QtWidgets import QMainWindow

from general.styleLoad import StyleLoad
from interface.settings import Settings


class SettingsLogic(QMainWindow, StyleLoad):
    def __init__(self):
        super().__init__()
        self.settingsInterface = Settings(self)

        self.label_segmento = self.settingsInterface.create_label("Segmento")
        self.label_amplitud = self.settingsInterface.create_label("Amplitud")
        self.text_segmento = self.settingsInterface.create_text()
        self.text_amplitud = self.settingsInterface.create_text()
        self.button_cancel = self.settingsInterface.create_button("Cancelar", self.cancel_execution)
        self.button_save = self.settingsInterface.create_button("Guardar", self.cancel_execution)

        self.mainWidget = self.settingsInterface.create_window()
        self.mainWidget.setLayout(self.settingsInterface.create_layout(self.label_segmento, self.label_amplitud, self.text_segmento, self.text_amplitud, self.button_cancel, self.button_save))
        self.setCentralWidget(self.mainWidget)

    def cancel_execution(self):
        self.close()



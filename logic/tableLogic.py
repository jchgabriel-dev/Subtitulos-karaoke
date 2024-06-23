from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from data.timerData import TimerData
from data.videoData import VideoData
from general.styleLoad import StyleLoad
from interface.table import Table
from logic.lineLogic import LineLogic


class TableLogic(QWidget, StyleLoad):
    def __init__(self):
        super().__init__()
        self.tableInterface = Table(self)
        self.video_data = VideoData()
        self.timer_data = TimerData()
        self.editionlabel = self.tableInterface.create_label()
        self.editionSwitch = self.tableInterface.create_switch(self.toggle_state)
        self.saveButton = self.tableInterface.create_button()
        self.contentScroll = self.tableInterface.create_scroll()
        self.layout_content = QVBoxLayout()

        self.setLayout(self.tableInterface.create_layout(self.editionlabel, self.editionSwitch, self.saveButton, self.contentScroll, self.layout_content))
        self.video_data.add_table_transcription(self)

    def update_table(self):
        for value in self.video_data.transcription:
            line = LineLogic()
            line.set_values(value["inicio"], value["fin"], value["texto"])
            self.layout_content.addWidget(line)

    def toggle_state(self, event):
        current_value = self.editionSwitch.value()
        new_value = 1 if current_value == 0 else 0
        self.editionSwitch.setValue(new_value)

        if self.editionSwitch.value() == 0:
            self.editionSwitch.setProperty("state", "inactive")
        else:
            self.editionSwitch.setProperty("state", "active")
        self.editionSwitch.style().polish(self.editionSwitch)


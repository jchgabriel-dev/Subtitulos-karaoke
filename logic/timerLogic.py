from PyQt5.QtWidgets import QWidget

from data.timerData import TimerData
from general.styleLoad import StyleLoad
from interface.timer import Timer


class TimerLogic(QWidget, StyleLoad):
    def __init__(self):
        super().__init__()
        self.timerInterface = Timer(self)
        self.seconds = self.timerInterface.create_label()

        self.setLayout(self.timerInterface.create_layout(self.seconds))

        self.timerData = TimerData()
        self.timerData.add_observer(self)

    def update_time(self, milliseconds):
        seconds, milliseconds = divmod(milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        self.seconds.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}")


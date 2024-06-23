from PyQt5.QtWidgets import QWidget

from general.styleLoad import StyleLoad
from interface.line import Line

class LineLogic(QWidget, StyleLoad):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineInterface = Line(self)

        self.button_add = self.lineInterface.create_button("add_button", "interface/icons/add.png", self.add_item)
        self.button_remove = self.lineInterface.create_button("delete_button", "interface/icons/delete.png", self.remove_item)
        self.text_input = self.lineInterface.create_text()
        self.start_input = self.lineInterface.create_time()
        self.end_input = self.lineInterface.create_time()

        self.setLayout(self.lineInterface.create_layout(self.button_add, self.button_remove, self.text_input, self.start_input, self.end_input))

    def add_item(self):
        new_item = LineLogic(self.parentWidget())
        self.parentWidget().layout().insertWidget(self.parentWidget().layout().indexOf(self) + 1, new_item)


    def remove_item(self):
        self.deleteLater()

    def set_values(self, start, end, text):
        print(start, end, text)
        minutesE = (end // 1000) // 60
        secondsE = (end // 1000) % 60
        end_str = "{:02d}:{:02d}".format(minutesE, secondsE)

        minutesS = (start // 1000) // 60
        secondsS = (start // 1000) % 60
        start_str = "{:02d}:{:02d}".format(minutesS, secondsS)

        self.start_input.setText(start_str)
        self.end_input.setText(end_str)
        self.text_input.setText(str(text))


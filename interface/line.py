from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLineEdit


class Line:
    def __init__(self, line):
        line.setAttribute(Qt.WA_StyledBackground, True)
        line.setObjectName("custom_item")

    def create_button(self, name, icon, function):
        button = QPushButton()
        button.setObjectName(name)
        button.setIcon(QIcon(icon))
        button.clicked.connect(function)
        return button

    def create_text(self):
        text = QLineEdit()
        text.setObjectName("text_line")
        return text

    def create_time(self):
        time = QLineEdit()
        time.setObjectName("text_time")
        time.setFixedWidth(60)
        return time

    def create_layout(self, buttonAdd, buttonRemove, text, start, end):
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 5, 8, 5)
        layout.addWidget(start)
        layout.addWidget(end)
        layout.addWidget(text)
        layout.addWidget(buttonAdd)
        layout.addWidget(buttonRemove)

        return layout
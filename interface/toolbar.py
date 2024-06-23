from asyncio import subprocess

from PyQt5.QtCore import QSize, Qt, QFile, QTextStream
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolButton, QFileDialog, QHBoxLayout, QWidget

class Toolbar:
    def __init__(self, toolbar):
        super().__init__()
        toolbar.setAttribute(Qt.WA_StyledBackground, True)
        toolbar.cargar_css("style/toolbarStyle.css")
        toolbar.setObjectName("toolbar_style")
        toolbar.setFixedHeight(70)

    def create_button(self, text, icon_path, function):
        button = QToolButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(30,30))
        button.setText(text)
        button.setFixedWidth(60)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setObjectName("button_style")
        button.clicked.connect(function)
        return button

    def create_layout(self, buttonNew, buttonOpen, buttonSave, buttonSeparate, buttonLyric, buttonSettings):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        layout.addWidget(buttonNew)
        layout.addWidget(buttonOpen)
        layout.addWidget(buttonSave)
        layout.addWidget(buttonSeparate)
        layout.addWidget(buttonLyric)
        layout.addWidget(buttonSettings)

        return layout









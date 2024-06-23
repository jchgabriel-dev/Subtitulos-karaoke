from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, \
    QPushButton, QLineEdit, QSlider

from data.videoData import VideoData
from general.styleLoad import StyleLoad


class Table:
    def __init__(self, table):
        super().__init__()
        table.setAttribute(Qt.WA_StyledBackground, True)
        table.setObjectName("table_style")
        table.cargar_css("style/tableStyle.css")
        table.setFixedHeight(350)

    def create_label(self):
        label = QLabel()
        label.setText("Edicion de letra: ")
        label.setObjectName("edition_style")
        return label

    def create_switch(self, toggle_state):
        switch = QSlider(Qt.Horizontal)
        switch.setFixedSize(50, 30)
        switch.setRange(0, 1)
        switch.setObjectName("slider_edition")
        switch.setProperty("state", "inactive")
        switch.mousePressEvent = toggle_state
        return switch

    def create_button(self):
        button = QPushButton()
        button.setText("Guardar")
        button.setFixedWidth(150)
        button.setObjectName("button_save")
        button.setFixedSize(QSize(120, 30))
        return button

    def create_scroll(self):
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        return scroll

    def create_layout(self, label, switch, button, scroll, layout):
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignHCenter)

        controlLayout = QHBoxLayout()
        controlLayout.setAlignment(Qt.AlignTop)

        container = QWidget()
        scroll.setWidget(container)
        layoutScroll = layout
        layoutScroll.setAlignment(Qt.AlignTop)
        layoutScroll.setContentsMargins(0, 0, 0, 0)
        layoutScroll.addWidget(label)
        container.setLayout(layoutScroll)

        saveLayout = QVBoxLayout()
        saveLayout.setAlignment(Qt.AlignCenter)
        saveLayout.addWidget(button)

        controlLayout.addWidget(label)
        controlLayout.addWidget(switch)

        mainLayout.addLayout(controlLayout)
        mainLayout.addWidget(scroll)
        mainLayout.addLayout(saveLayout)
        return mainLayout





from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QHBoxLayout


class Graph(QWidget):
    def __init__(self, graph):
        super().__init__()
        graph.setAttribute(Qt.WA_StyledBackground, True)
        graph.cargar_css("style/graphStyle.css")
        graph.setObjectName("graph_style")

    def create_timeline(self, paintEvent, wheelEvent):
        timeline = QWidget()
        timeline.paintEvent = paintEvent
        timeline.wheelEvent = wheelEvent

        return timeline

    def create_scroll(self):
        scroll = QScrollArea()
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        return scroll


    def create_layout(self, timeline, scroll, marker):
        layoutMain = QVBoxLayout()
        layoutScroll = QVBoxLayout()
        layoutTimeline = QHBoxLayout()

        container = QWidget()
        scroll.setWidget(container)
        layoutScroll.addWidget(timeline)
        layoutScroll.setContentsMargins(0, 0, 0, 0)

        layoutTimeline.setContentsMargins(0, 0, 0, 0)
        layoutTimeline.addWidget(marker)
        timeline.setLayout(layoutTimeline)

        container.setLayout(layoutScroll)
        layoutMain.addWidget(scroll)

        return layoutMain


class TimelineItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, parent.height())
        self.dragging = False
        self.start_pos = None
        self.pos = 0

        """
        audio_data = np.sin(2 * np.pi * np.linspace(0, 1, 1000))

        self.figure, self.ax = plt.subplots()
        self.ax.plot(audio_data)
        self.ax.axis('off')

        self.canvas = FigureCanvas(self.figure)
        self.Vlayout.addWidget(self.canvas)
        self.figure.tight_layout()
        self.canvas.mpl_connect('scroll_event', self.zoom_horizontal)



    def zoom_horizontal(self, event):
        if event.button == 'up':
            x_min, x_max = self.ax.get_xlim()
            x_range = x_max - x_min
            new_x_range = x_range * 0.9
            center_x = (x_min + x_max) / 2
            self.ax.set_xlim(center_x - new_x_range / 2, center_x + new_x_range / 2)
        elif event.button == 'down':
            x_min, x_max = self.ax.get_xlim()
            x_range = x_max - x_min
            new_x_range = x_range * 1.1
            center_x = (x_min + x_max) / 2
            self.ax.set_xlim(center_x - new_x_range / 2, center_x + new_x_range / 2)

        self.canvas.draw()

"""
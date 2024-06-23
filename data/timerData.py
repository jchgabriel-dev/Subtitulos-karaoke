from PyQt5.QtCore import QTime, QTimer, QElapsedTimer, pyqtSignal, QObject, QThread
import time


class TimerData(QObject):
    _instance = None

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.elapsed_timer = QElapsedTimer()
        self.time_amount = 0
        self.time = 0
        self.is_running = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TimerData, cls).__new__(cls)
            cls._instance.observers = []
        return cls._instance

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.elapsed_timer.start()
            self.timer.start(1)

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.timer.stop()
            self.time_amount += self.elapsed_timer.elapsed()

    def reset(self):
        self.time_amount = 0
        self.time = 0

    def update(self):
        if self.is_running:
            self.time = self.elapsed_timer.elapsed() + self.time_amount
            self.notifiy_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notifiy_observers(self):
        for observer in self.observers:
            observer.update_time(self.time)

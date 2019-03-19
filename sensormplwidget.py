from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SensorMplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(figsize=(12, 9)))
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)
        self.setLayout(self.vertical_layout)
        self.canvas.axes1 = self.canvas.figure.add_subplot(211)
        self.canvas.axes1.spines["top"].set_visible(False)
        self.canvas.axes1.spines["right"].set_visible(False)
        self.canvas.axes1.get_xaxis().tick_bottom()
        self.canvas.axes1.get_yaxis().tick_left()
        self.canvas.axes1.set_ylabel("Temperature", fontsize=12)
        self.canvas.axes1.tick_params(axis='both', labelsize=10)
        self.canvas.axes1.set_yticks(range(50, 501, 50))
        self.canvas.axes1.set_xticks(range(-50, 51, 10))
        self.canvas.axes2 = self.canvas.figure.add_subplot(212)
        self.canvas.axes2.spines["top"].set_visible(False)
        self.canvas.axes2.spines["right"].set_visible(False)
        self.canvas.axes2.get_xaxis().tick_bottom()
        self.canvas.axes2.get_yaxis().tick_left()
        self.canvas.axes2.set_xlabel("Time", fontsize=12)
        self.canvas.axes2.set_ylabel("Pressure", fontsize=12)
        self.canvas.axes2.tick_params(axis='both', labelsize=10)
        self.canvas.axes2.set_yticks(range(50, 501, 50))
        self.canvas.axes2.set_xticks(range(-50, 51, 10))
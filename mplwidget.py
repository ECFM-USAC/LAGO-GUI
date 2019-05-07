from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(figsize=(12, 9)))
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(self.vertical_layout)
        self.canvas.axes.spines["top"].set_visible(False)
        self.canvas.axes.spines["right"].set_visible(False)
        self.canvas.axes.get_xaxis().tick_bottom()
        self.canvas.axes.get_yaxis().tick_left()
        self.canvas.axes.set_xlabel("Maximum Amplitude", fontsize=16)
        self.canvas.axes.set_ylabel("Count", fontsize=16)
        self.canvas.axes.tick_params(axis='both', labelsize=14)
        self.canvas.axes.set_yticks(range(50, 501, 50))
        self.canvas.axes.set_xticks(range(0, 16385, 2048))

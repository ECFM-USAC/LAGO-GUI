from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import WnMain, WnSerial, WnTCP
from tserialThread import tserialThreadClass
from tcpClientThread import tcpClientThreadClass

import numpy as np


class MainClass(QMainWindow,WnMain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushstartSerial.clicked.connect(self.btnStartSClicked)
        self.pushstopSerial.clicked.connect(self.btnStopSClicked)
        self.pushclearserial.clicked.connect(self.btnClearSClicked)
        self.pushtcpconnect.clicked.connect(self.btnConnectClicked)
        self.pushtcpclear.clicked.connect(self.btnCleartClicked)
        self.pushtcpdisconnect.clicked.connect(self.btnStopTClicked)
        self.pushHistoStart.clicked.connect(self.histo_graph)
        self.pushSensorStart.clicked.connect(self.sensor_graph)
        self.pushTSStart.clicked.connect(self.timestamp_graph)


    def histo_graph(self):
        data = np.random.laplace(loc=15, scale=3, size=5000)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.spines["top"].set_visible(False)
        self.MplWidget.canvas.axes.spines["right"].set_visible(False)
        self.MplWidget.canvas.axes.get_xaxis().tick_bottom()
        self.MplWidget.canvas.axes.get_yaxis().tick_left()
        self.MplWidget.canvas.axes.set_xlabel("Maximum Amplitude", fontsize=16)
        self.MplWidget.canvas.axes.set_ylabel("Count", fontsize=16)
        self.MplWidget.canvas.axes.tick_params(axis='both', labelsize=14)
        self.MplWidget.canvas.axes.hist(data, bins='auto', color="#3F5D7D")
        self.MplWidget.canvas.axes.set_yticks(range(50, 501, 50))
        self.MplWidget.canvas.axes.set_xticks(range(-50, 51, 10))
        self.MplWidget.canvas.draw()

    def sensor_graph(self):
        sensorT = np.random.normal(size=100)
        sensorP = np.random.logistic(size=100)
        self.SensorMplWidget.canvas.axes1.clear()
        self.SensorMplWidget.canvas.axes2.clear()
        self.SensorMplWidget.canvas.axes1.spines["top"].set_visible(False)
        self.SensorMplWidget.canvas.axes1.spines["right"].set_visible(False)
        self.SensorMplWidget.canvas.axes1.get_xaxis().tick_bottom()
        self.SensorMplWidget.canvas.axes1.get_yaxis().tick_left()
        self.SensorMplWidget.canvas.axes1.set_ylabel("Temperature", fontsize=12)
        self.SensorMplWidget.canvas.axes1.plot(sensorT, color="#3F5D7D")
        self.SensorMplWidget.canvas.axes2.spines["top"].set_visible(False)
        self.SensorMplWidget.canvas.axes2.spines["right"].set_visible(False)
        self.SensorMplWidget.canvas.axes2.get_xaxis().tick_bottom()
        self.SensorMplWidget.canvas.axes2.get_yaxis().tick_left()
        self.SensorMplWidget.canvas.axes2.set_xlabel("Time", fontsize=12)
        self.SensorMplWidget.canvas.axes2.set_ylabel("Pressure", fontsize=12)
        self.SensorMplWidget.canvas.axes2.plot(sensorP, color="#3F5D7D")

        self.SensorMplWidget.canvas.draw()

    def timestamp_graph(self):
        timestamp = np.random.normal(size=30)
        self.TSMplWidget.canvas.axes.clear()
        self.TSMplWidget.canvas.axes.spines["top"].set_visible(False)
        self.TSMplWidget.canvas.axes.spines["right"].set_visible(False)
        self.TSMplWidget.canvas.axes.get_xaxis().tick_bottom()
        self.TSMplWidget.canvas.axes.get_yaxis().tick_left()
        self.TSMplWidget.canvas.axes.hist(timestamp, color="#3F5D7D", bins=100)
        self.TSMplWidget.canvas.axes.set_xlabel("Count", fontsize=16)
        self.TSMplWidget.canvas.axes.set_ylabel("Time", fontsize=16)
        self.TSMplWidget.canvas.draw()


    def btnStartSClicked(self):
        wserial.openWindow()

    def btnStopSClicked(self):
        self.serialTextEdit.clear()
        wserial.close()
        wserial.mySerial.terminate()
        self.pushstartSerial.setEnabled(True)
        self.pushstopSerial.setEnabled(False)

    def btnStopTClicked(self):
        self.tcpTextEdit.clear()
        wtcp.myTCPClient.close()
        wtcp.myTCPClient.terminate()
        self.pushtcpconnect.setEnabled(True)
        self.pushtcpdisconnect.setEnabled(False)

    def btnClearSClicked(self):
        self.serialTextEdit.clear()

    def btnConnectClicked(self):
        wtcp.openWindow()

    def btnCleartClicked(self):
        self.tcpTextEdit.clear()


class SerialWindow(QDialog,WnSerial.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.window = QDialog()
        self.ui = WnSerial.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.buttonBoxOk.accepted.connect(self.btnClickedOk)
        self.ui.buttonBoxCancel.rejected.connect(self.btnClickedCancel)

    def ssetup(self):
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox_5.clear()
        stopbits = ["1 Bit", "1.5 Bits", "2 Bits"];
        self.ui.comboBox_4.addItems(stopbits)
        self.ui.comboBox_4.setCurrentIndex(0)

        checks = ["None", "Odd", "Even"]
        self.ui.comboBox_5.addItems(checks)
        self.ui.comboBox_5.setCurrentIndex(0)

        ports = tserialThreadClass.get_ports(self)
        self.ui.comboBox.addItems(ports)

        bauds = ["50", "75", "134", "110", "150", "200", "300", "600", "1200", "2400", "4800", "9600", "14400", "19200",
                 "38400", "56000", "57600",
                 "115200"];
        self.ui.comboBox_2.addItems(bauds)
        self.ui.comboBox_2.setCurrentIndex(11)

        bits = ["5 Bits", "6 Bits", "7 Bits", "8 Bits"]
        self.ui.comboBox_3.addItems(bits)
        self.ui.comboBox_3.setCurrentIndex(len(bits) - 1)

    def openWindow(self):
        wserial.ssetup()
        self.window.show()

    def btnClickedOk(self):
        wmain.serialTextEdit.clear()
        self.serialport=str(self.ui.comboBox.currentText())
        self.baudrate=str(self.ui.comboBox_2.currentText())
        self.databits=str(self.ui.comboBox_3.currentText())
        self.stopbits=str(self.ui.comboBox_4.currentText())
        self.parity=str(self.ui.comboBox_5.currentText())
        self.mySerial=tserialThreadClass()
        self.flag=self.mySerial.serialSetup(self.baudrate,self.serialport, self.databits, self.stopbits, self.parity)
        if (self.flag==1):
            self.mySerial.mesaj.connect(wmain.serialTextEdit.append)
            self.mySerial.start()
            wmain.pushstopSerial.setEnabled(True)
            wmain.pushstartSerial.setEnabled(False)
        else:
            wmain.serialTextEdit.append("Port not available")
        self.window.close()

    def btnClickedCancel(self):
        self.ui.comboBox.clear()
        self.window.close()

class TCPWindow(QDialog,WnTCP.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.window = QDialog()
        self.ui = WnTCP.Ui_Dialog()
        self.ui.setupUi(self.window)

        self.ui.buttonBoxOk.accepted.connect(self.btnClickedOk)
        self.ui.buttonBoxCancel.rejected.connect(self.btnClickedCancel)

    def openWindow(self):
        self.window.show()
        self.ui.tiplineedit.setFocus()

    def btnClickedOk(self):
        wmain.tcpTextEdit.clear()
        self.tcpIP=self.ui.tiplineedit.text()
        self.tcpPort=self.ui.tportlineedit.text()
        self.myTCPClient=tcpClientThreadClass()
        self.window.close()
        self.flag=self.myTCPClient.tcpSetup(self.tcpIP,self.tcpPort)

        if (self.flag==1):
            wmain.tcpTextEdit.append("Server Found")
            self.myTCPClient.tcpmess.connect(wmain.tcpTextEdit.append)
            self.myTCPClient.start()
            wmain.pushtcpdisconnect.setEnabled(True)
            wmain.pushtcpconnect.setEnabled(False)
        else:
            wmain.tcpTextEdit.append("Server not available")

    def btnClickedCancel(self):
        self.window.close()


if __name__ == "__main__":
    appgui = QApplication(sys.argv)
    wmain= MainClass()
    wserial = SerialWindow()
    wtcp=TCPWindow()
    wmain.show()
    appgui.exec_()

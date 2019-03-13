from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import WnMain, WnSerial, WnTCP
from tserialThread import tserialThreadClass
from tcpClientThread import tcpClientThreadClass



class MainClass(QMainWindow,WnMain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushstartSerial.clicked.connect(self.btnStartSClicked)
        self.pushstopSerial.clicked.connect(self.btnStopSClicked)
        self.pushclearserial.clicked.connect(self.btnClearSClicked)
        self.pushtcpconnect.clicked.connect(self.btnConnectClicked)

    def btnStartSClicked(self):
        wserial.openWindow()

    def btnStopSClicked(self):
        self.serialTextEdit.clear()
        wserial.mySerial.terminate()
        self.pushstartSerial.setEnabled(True)
        self.pushstopSerial.setEnabled(False)

    def btnClearSClicked(self):
        self.serialTextEdit.clear()


    def btnConnectClicked(self):
        wntcp.openWindow()


    def btnClear2Clicked(self):
        self.textEdit_2.clear()


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
        self.flag=self.myTCPClient.tcpSetup(self.tcpIP,self.tcpPort)
        if (self.flag==1):
            wmain.tcpTextEdit.append("Server Found")
            #self.myTCPClient.tcpmess.connect(wmain.tcpTextEdit.append)
            #self.myTCPClient.start()
            #wmain.pushtcpconnect.setEnabled(False)
        else:
            wmain.tcpTextEdit.append("Server not available")
        self.window.close()



    def btnClickedCancel(self):
        self.window.close()




if __name__ == "__main__":
    appgui = QApplication(sys.argv)
    wmain= MainClass()
    wserial = SerialWindow()
    wntcp=TCPWindow()
    wmain.show()
    appgui.exec_()

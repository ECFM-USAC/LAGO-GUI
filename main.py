from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import WnMain, WnSerial, WnTCP
from tserialThread import tserialThreadClass
from tcpClientThread import tcpClientThreadClass

import numpy as np
import statistics as sts


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
        self.updatebutton.clicked.connect(self.btnUpdateClicked)
        self.TmaxA=0
        self.PmaxA=0
        self.TminA=100
        self.PminA=100


    def histo_graph(self):
        count = TCPWindow.hdata
        self.maxvalue=np.amax(count)
        self.MaxVLineEdit.setText(str(self.maxvalue))
        self.median = sts.median(count)
        self.MedianLineEdit.setText(str(self.median))
        self.variance = sts.pvariance(count)
        self.VarianceLineEdit.setText(str(self.variance))
        self.mean = sts.mean(count)
        self.MeanLineEdit.setText(str(self.mean))
        self.mode = np.argmax(count)
        self.ModeLineEdit.setText(str(self.mode))
        self.sdev = sts.stdev(count)
        self.StandardDLineEdit.setText(str(round(self.sdev,10)))
        self.summation=np.sum(count)
        self.SummLineEdit.setText((str(self.summation)))

        self.rms = np.sqrt(np.mean(count** 2))
        self.RMSLineEdit.setText((str(self.rms)))

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.spines["top"].set_visible(False)
        self.MplWidget.canvas.axes.spines["right"].set_visible(False)
        self.MplWidget.canvas.axes.get_xaxis().tick_bottom()
        self.MplWidget.canvas.axes.get_yaxis().tick_left()
        self.MplWidget.canvas.axes.set_xlabel("Maximum Amplitude", fontsize=16)
        self.MplWidget.canvas.axes.set_ylabel("Count", fontsize=16)
        self.MplWidget.canvas.axes.tick_params(axis='both', labelsize=14)
        self.MplWidget.canvas.axes.plot(count, color="#3F5D7D")
#        self.MplWidget.canvas.axes.hist(range(16383), 16383, weights=count, color="#3F5D7D")
        self.MplWidget.canvas.axes.set_yticks(range(0, 501, 50))
        self.MplWidget.canvas.axes.set_xticks(range(0, 16385, 2048))
        self.MplWidget.canvas.draw()

    def sensor_graph(self):
        self.lcdNumber.display(str(TCPWindow.tsdata[59]))
        self.lcdNumber_2.display(str(TCPWindow.psdata[59]))

        self.Tmax=np.max(TCPWindow.tsdata)
        if(self.Tmax>self.TmaxA):
            self.TmaxA=self.Tmax
        self.MaxVTLineEdit.setText(str(self.TmaxA))

        self.Pmax=np.max(TCPWindow.psdata)
        if (self.Pmax > self.PmaxA):
            self.PmaxA = self.Pmax
        self.MaxVPLineEdit.setText(str(self.PmaxA))

        self.Tmin=np.min(TCPWindow.tsdata)
        if(self.Tmin==0):
            self.Tmin=TCPWindow.tsdata[59]
        if(self.Tmin<self.TminA):
            self.TminA=self.Tmin
        self.MinTVLineEdit.setText(str(self.TminA))

        self.Pmin=np.min(TCPWindow.psdata)
        if(self.Pmin==0):
            self.Pmin=TCPWindow.psdata[59]
        if (self.Pmin < self.PminA):
            self.PminA = self.Pmin
        self.MinPVLineEdit.setText(str(self.PminA))

        self.Tpasttrend=np.sum(TCPWindow.tsdata[40:49])
        self.Tprestrend=np.sum(TCPWindow.tsdata[50:59])
        self.TTrend=self.Tpasttrend-self.Tprestrend
        if(self.TTrend<0):
            self.ADFTLineEdit.setText("Rising")
        elif(self.TTrend>0):
            self.ADFTLineEdit.setText("Falling")
        elif(self.TTrend==0):
            self.ADFTLineEdit.setText("Fixed")

        self.Ppasttrend = np.sum(TCPWindow.psdata[40:49])
        self.Pprestrend = np.sum(TCPWindow.psdata[50:59])
        self.PTrend = self.Ppasttrend - self.Pprestrend
        if (self.PTrend < 0):
            self.ADFPLineEdit.setText("Rising")
        elif (self.PTrend > 0):
            self.ADFPLineEdit.setText("Falling")
        elif (self.PTrend == 0):
            self.ADFPLineEdit.setText("Fixed")

        self.Tmean=round(np.mean(TCPWindow.tsdata),4)
        self.MeanTLineEdit.setText(str(self.Tmean))
        self.Pmean=round(np.mean(TCPWindow.psdata),4)
        self.MeanPLineEdit.setText(str(self.Pmean))

        self.SensorMplWidget.canvas.axes1.clear()
        self.SensorMplWidget.canvas.axes2.clear()
        self.SensorMplWidget.canvas.axes1.spines["top"].set_visible(False)
        self.SensorMplWidget.canvas.axes1.spines["right"].set_visible(False)
        self.SensorMplWidget.canvas.axes1.get_xaxis().tick_bottom()
        self.SensorMplWidget.canvas.axes1.get_yaxis().tick_left()
        self.SensorMplWidget.canvas.axes1.set_ylabel("Temperature (°C)", fontsize=12)
        self.SensorMplWidget.canvas.axes1.plot(range(-60,0), TCPWindow.tsdata, color="#3F5D7D")
        self.SensorMplWidget.canvas.axes2.spines["top"].set_visible(False)
        self.SensorMplWidget.canvas.axes2.spines["right"].set_visible(False)
        self.SensorMplWidget.canvas.axes2.get_xaxis().tick_bottom()
        self.SensorMplWidget.canvas.axes2.get_yaxis().tick_left()
        self.SensorMplWidget.canvas.axes2.set_xlabel("Time (s)", fontsize=12)
        self.SensorMplWidget.canvas.axes2.set_ylabel("Pressure (hPa) ", fontsize=12)
        self.SensorMplWidget.canvas.axes2.plot(range(-60,0), TCPWindow.psdata, color="#3F5D7D")
        self.SensorMplWidget.canvas.draw()

    def osc_graph(self):
        self.oscidata = TCPWindow.oscdata
        self.TSMplWidget.canvas.axes.clear()
        self.TSMplWidget.canvas.axes.spines["top"].set_visible(False)
        self.TSMplWidget.canvas.axes.spines["right"].set_visible(False)
        self.TSMplWidget.canvas.axes.get_xaxis().tick_bottom()
        self.TSMplWidget.canvas.axes.get_yaxis().tick_left()
        self.TSMplWidget.canvas.axes.plot(self.oscidata, color="#3F5D7D")
        self.TSMplWidget.canvas.axes.set_xlabel("Time (s)", fontsize=16)
        self.TSMplWidget.canvas.axes.set_ylabel("Voltage (V)", fontsize=16)
        self.TSMplWidget.canvas.draw()

    def btnUpdateClicked(self):
        self.thrvalue = self.spinBoxVT.value()
        self.dacvalue = self.spinBoxVL.value()
        self.decfvalue = self.spinBoxDF.value()
        wtcp.myTCPClient.updateV(self.thrvalue, self.dacvalue, self.decfvalue)


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
        self.updatebutton.setEnabled((False))

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
        TCPWindow.hdata=[]
        TCPWindow.tsdata=[0]*60
        TCPWindow.psdata=[0]*60
        TCPWindow.oscdata=[]

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
            wmain.tcpTextEdit.append("Connection Established")
            self.myTCPClient.tcpmess.connect(wmain.tcpTextEdit.append)
            self.myTCPClient.start()
            self.myTCPClient.hraw_data.connect(self.dataGetH)
            self.myTCPClient.raw_osc.connect(self.dataGetOsc)
            self.myTCPClient.tsraw_data.connect(self.dataGetTS)
            self.myTCPClient.psraw_data.connect(self.dataGetPS)
            self.myTCPClient.raw_time.connect(self.dataGetTime)


            wmain.pushtcpdisconnect.setEnabled(True)
            wmain.pushtcpconnect.setEnabled(False)
            wmain.updatebutton.setEnabled(True)
        else:
            wmain.tcpTextEdit.append("Server not available")

    def btnClickedCancel(self):
        self.window.close()

    def dataGetH(self, value):
        self.raw=value
        TCPWindow.hdata=np.fromstring(self.raw, dtype=int, sep='\n')
        if(len(TCPWindow.hdata)>10):
            wmain.histo_graph()
        return

    def dataGetOsc(self, value):
        self.rawosc=value
        TCPWindow.oscdata = np.fromstring(self.rawosc, dtype=int, sep='\n')
        wmain.osc_graph()
        return


    def dataGetTS(self, value):
        self.raw=value
        TCPWindow.tsdata.append(int(self.raw))
        TCPWindow.tsdata.pop(0)
        return

    def dataGetPS(self, value):
        self.raw=value
        TCPWindow.psdata.append(int(self.raw))
        TCPWindow.psdata.pop(0)
        wmain.sensor_graph()
        return

    def dataGetTime(self, value):
        self.time=value
        self.year=str(self.time[0:4])
        self.month=str(self.time[6:7])
        self.day=str(self.time[8:10])
        self.hours=str(self.time[11:13])


        self.minutes=str(self.time[14:16])
        self.seconds=str(self.time[17:19])
        self.lhours=int(self.hours)-6
        if(self.lhours<0):
            self.lhours=(self.lhours+24)

        wmain.yearlabel.setText(self.year)
        wmain.daylabel.setText(self.day)
        if(int(self.month)==1):
            wmain.monthlabel.setText("January")
        elif(int(self.month)==2):
            wmain.monthlabel.setText("February")
        elif(int(self.month)==3):
            wmain.monthlabel.setText("March")
        elif(int(self.month)==4):
            wmain.monthlabel.setText("April")
        elif(int(self.month)==5):
            wmain.monthlabel.setText("May")
        elif(int(self.month)==6):
            wmain.monthlabel.setText("June")
        elif(int(self.month)==7):
            wmain.monthlabel.setText("July")
        elif(int(self.month)==8):
            wmain.monthlabel.setText("August")
        elif(int(self.month)==9):
            wmain.monthlabel.setText("September")
        elif(int(self.month)==10):
            wmain.monthlabel.setText("October")
        elif(int(self.month)==11):
            wmain.monthlabel.setText("November")
        elif(int(self.month)==12):
            wmain.monthlabel.setText("December")

        wmain.LCDUHH.display(int(self.hours))
        wmain.LCDUMM.display(int(self.minutes))
        wmain.LCDUSS.display(int(self.seconds))
        wmain.LCDLHH.display(int(self.lhours))
        wmain.LCDLMM.display(int(self.minutes))
        wmain.LCDLSS.display(int(self.seconds))
        return

if __name__ == "__main__":
    appgui = QApplication(sys.argv)
    wmain= MainClass()
    wserial = SerialWindow()
    wtcp=TCPWindow()
    wmain.show()
    appgui.exec_()

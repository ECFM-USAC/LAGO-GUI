import socket
from PyQt5.QtCore import pyqtSignal,QThread
import time

class tcpClientThreadClass(QThread):
    hraw_data=pyqtSignal(str)
    tsraw_data = pyqtSignal(str)
    psraw_data = pyqtSignal(str)
    tcpmess=pyqtSignal(str)
    raw_time=pyqtSignal(str)
    raw_osc=pyqtSignal(str)

    def __init__(self,parent=None):
        super(tcpClientThreadClass,self).__init__(parent)


    def tcpSetup(self,ip,port):
        self.port = port
        self.ip = ip
        self.tflag = 0

        self.clientTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientTCP.settimeout(1)

        try:
            self.port=int(self.port)
            self.clientTCP.connect((self.ip, self.port))
            self.clientTCP.settimeout(None)
            return 1
        except:
            return 0


    def run(self):
        while True:
            try:
###Datos Histograma
                self.clientTCP.send('data'.encode())
                self.hdata=[]
                while True:
                    self.buffer = self.clientTCP.recv(511).decode('utf-8')
                    if(len(self.buffer)<511):
                        self.hdata.append(self.buffer)
                        break
                    else:
                        self.hdata.append(self.buffer)

                self.histostr="".join(self.hdata)
                self.hraw_data.emit(self.histostr)

###Datos Osciloscopio
                self.clientTCP.send('osc'.encode())
                self.oscdata=[]
                while True:
                    self.buffer = self.clientTCP.recv(511).decode('utf-8')
                    if(len(self.buffer)<511):
                        self.oscdata.append(self.buffer)
                        break
                    else:
                        self.oscdata.append(self.buffer)

                self.oscostr="".join(self.oscdata)
                self.raw_osc.emit(self.oscostr)


                self.clientTCP.send('sensorT'.encode())
                self.buffer2 = self.clientTCP.recv(128).decode('utf-8')
                self.tsraw_data.emit(str(self.buffer2))

                self.clientTCP.send('sensorP'.encode())
                self.buffer3 = self.clientTCP.recv(128).decode('utf-8')
                self.psraw_data.emit(str(self.buffer3))

                self.clientTCP.send('timestamp'.encode())
                self.buffer4 = self.clientTCP.recv(128).decode('utf-8')
                self.raw_time.emit(str(self.buffer4))


                time.sleep(1)

            except Exception as e:
                self.tcpmess.emit(str("Something's wrong with %s:%d. Exception is %s" % (self.ip, self.port, e)))


    def updateV(self, thr, dac, decf):
        self.vthreshold= thr
        self.vlevel=dac
        self.decfactor=decf


        self.clientTCP.send("thr_write".encode())
        time.sleep(0.1)
        self.clientTCP.send((str(self.vthreshold)+'\r').encode())
        time.sleep(0.1)
        self.clientTCP.send("dac_write".encode())
        time.sleep(0.1)
        self.clientTCP.send((str(self.vlevel)+'\r').encode())
        time.sleep(0.1)
        self.clientTCP.send("dec_factor".encode())
        time.sleep(0.1)
        self.clientTCP.send((str(self.decfactor)+'\r').encode())



    def close(self):
        self.tcpmess.emit(str("Connection Closed"))
        self.clientTCP.close()

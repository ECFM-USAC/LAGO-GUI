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

                #self.clientTCP.send('data'.encode())
                #self.buffer1 = self.clientTCP.recv(65535).decode('utf-8')
                #self.buffer1=self.buffer1.strip()
                #self.hraw_data.emit(self.buffer1)



                self.clientTCP.send('osc'.encode())
                self.buffer5 = self.clientTCP.recv(128).decode('utf-8')
                self.buffer5=self.buffer5.strip()
                self.raw_osc.emit(self.buffer5)


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


    def close(self):
        self.tcpmess.emit(str("Connection Closed"))
        self.clientTCP.close()

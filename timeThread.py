import socket
from PyQt5.QtCore import pyqtSignal,QThread
import time


class timeThreadClass(QThread):


    def __init__(self,parent=None):
        super(timeThreadClass,self).__init__(parent)

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
                self.clientTCP.connect((self.ip, self.port))
                comando = self.clientTCP.recv(20)
                comando=str(comando,'utf-8')
                self.tcpmess.emit(str(comando))

            except Exception as e:
                self.tcpmess.emit(str("something's wrong with %s:%d. Exception is %s" % (self.ip, self.port, e)))
            finally:
                self.clientTCP.close()
                self.terminate()

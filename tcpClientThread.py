import socket
from PyQt5.QtCore import pyqtSignal,QThread

class tcpClientThreadClass(QThread):
    tcpmess=pyqtSignal(str)

    def __init__(self,parent=None):
        super(tcpClientThreadClass,self).__init__(parent)


    def tcpSetup(self,ip,port):
        self.port = int(port)
        self.ip = ip
        self.tflag = 0

        self.clientTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.clientTCP.connect((self.ip, self.port))
            return 1
        except:
            return 0


    def run(self):
        while True:
            comando = self.clientTCP.recv()
            self.tcpmess.emit(str(comando))
            print(comando)


import serial
import sys
import glob
from PyQt5.QtCore import pyqtSignal,QThread

class tserialThreadClass(QThread):
    mesaj=pyqtSignal(str)

    def __init__(self,parent=None):
        super(tserialThreadClass,self).__init__(parent)
        self.serport=serial.Serial()


    def serialSetup(self,baud,port,databits,stop, par):
        self.serport.port=port
        self.serport.baudrate=baud
        self.databits=databits
        if(self.databits=="5 Bits"):
            self.serport.bytesize=serial.FIVEBITS
        elif(self.databits=="6 Bits"):
            self.serport.bytesize=serial.SIXBITS
        elif(self.databits=="7 Bits"):
            self.serport.bytesize=serial.SEVENBITS
        elif(self.databits=="8 Bits"):
            self.serport.bytesize=serial.EIGHTBITS

        self.stop=stop
        if(self.stop=="1 Bit"):
            self.serport.stopbits=serial.STOPBITS_ONE
        elif(self.stop=="1.5 Bits"):
            self.serport.stopbits=serial.STOPBITS_ONE_POINT_FIVE
        elif(self.stop=="2 Bits"):
            self.serport.stopbits=serial.STOPBITS_TWO


        self.par=par
        if(self.par=="None"):
            self.serport.parity=serial.PARITY_NONE
        elif(self.par=="Odd"):
            self.serport.parity=serial.PARITY_ODD
        elif(self.par=="Even"):
            self.serport.parity=serial.PARITY_EVEN

        self.sflag = 0

        try:
            self.serport.open()
            return 1
        except:
            return 0

    def run(self):
        while True:
            msj=self.serport.readline()
            self.mesaj.emit(str(msj))

    def get_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result=[]

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def sclose(self):
        self.serport.close()
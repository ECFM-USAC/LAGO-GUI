# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WnMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1303, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1281, 701))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 720, 641, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 17))
        self.label.setObjectName("label")
        self.tcpTextEdit = QtWidgets.QTextEdit(self.frame)
        self.tcpTextEdit.setGeometry(QtCore.QRect(10, 30, 521, 101))
        self.tcpTextEdit.setReadOnly(True)
        self.tcpTextEdit.setObjectName("tcpTextEdit")
        self.pushtcpconnect = QtWidgets.QPushButton(self.frame)
        self.pushtcpconnect.setGeometry(QtCore.QRect(540, 40, 89, 25))
        self.pushtcpconnect.setObjectName("pushtcpconnect")
        self.pushtcpclear = QtWidgets.QPushButton(self.frame)
        self.pushtcpclear.setGeometry(QtCore.QRect(540, 90, 89, 25))
        self.pushtcpclear.setObjectName("pushtcpclear")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(650, 720, 641, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.serialTextEdit = QtWidgets.QTextEdit(self.frame_2)
        self.serialTextEdit.setGeometry(QtCore.QRect(10, 30, 521, 101))
        self.serialTextEdit.setReadOnly(True)
        self.serialTextEdit.setObjectName("serialTextEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.label_2.setObjectName("label_2")
        self.pushclearserial = QtWidgets.QPushButton(self.frame_2)
        self.pushclearserial.setGeometry(QtCore.QRect(540, 100, 89, 25))
        self.pushclearserial.setObjectName("pushclearserial")
        self.pushstartSerial = QtWidgets.QPushButton(self.frame_2)
        self.pushstartSerial.setGeometry(QtCore.QRect(540, 40, 89, 25))
        self.pushstartSerial.setObjectName("pushstartSerial")
        self.pushstopSerial = QtWidgets.QPushButton(self.frame_2)
        self.pushstopSerial.setEnabled(False)
        self.pushstopSerial.setGeometry(QtCore.QRect(540, 70, 89, 25))
        self.pushstopSerial.setObjectName("pushstopSerial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LAGO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 3"))
        self.label.setText(_translate("MainWindow", "TCP Connection"))
        self.pushtcpconnect.setText(_translate("MainWindow", "Connect"))
        self.pushtcpclear.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Serial Log"))
        self.pushclearserial.setText(_translate("MainWindow", "Clear"))
        self.pushstartSerial.setText(_translate("MainWindow", "Connect"))
        self.pushstopSerial.setText(_translate("MainWindow", "Disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WnSerial.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(224, 312)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 120, 86, 25))
        self.comboBox_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 67, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 70, 86, 25))
        self.comboBox_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label.setObjectName("label")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 170, 86, 25))
        self.comboBox_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 67, 17))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 20, 86, 25))
        self.comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 220, 86, 25))
        self.comboBox_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 67, 17))
        self.label_4.setObjectName("label_4")
        self.buttonBoxOk = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxOk.setGeometry(QtCore.QRect(20, 270, 81, 25))
        self.buttonBoxOk.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBoxOk.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOk.setObjectName("buttonBoxOk")
        self.buttonBoxCancel = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxCancel.setGeometry(QtCore.QRect(110, 270, 81, 25))
        self.buttonBoxCancel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBoxCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBoxCancel.setObjectName("buttonBoxCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.comboBox_3)
        Dialog.setTabOrder(self.comboBox_3, self.comboBox_4)
        Dialog.setTabOrder(self.comboBox_4, self.comboBox_5)
        Dialog.setTabOrder(self.comboBox_5, self.buttonBoxOk)
        Dialog.setTabOrder(self.buttonBoxOk, self.buttonBoxCancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Data bits"))
        self.label.setText(_translate("Dialog", "Port"))
        self.label_5.setText(_translate("Dialog", "Parity"))
        self.label_2.setText(_translate("Dialog", "Baudrate"))
        self.label_4.setText(_translate("Dialog", "Stop bits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


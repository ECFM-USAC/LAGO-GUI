# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WnTCP.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(163, 162)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.buttonBoxOk = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxOk.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.buttonBoxOk.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBoxOk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBoxOk.setAutoFillBackground(False)
        self.buttonBoxOk.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxOk.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOk.setCenterButtons(True)
        self.buttonBoxOk.setObjectName("buttonBoxOk")
        self.tiplineedit = QtWidgets.QLineEdit(Dialog)
        self.tiplineedit.setGeometry(QtCore.QRect(10, 30, 141, 25))
        self.tiplineedit.setObjectName("tiplineedit")
        self.tportlineedit = QtWidgets.QLineEdit(Dialog)
        self.tportlineedit.setGeometry(QtCore.QRect(10, 80, 141, 25))
        self.tportlineedit.setObjectName("tportlineedit")
        self.buttonBoxCancel = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxCancel.setGeometry(QtCore.QRect(80, 120, 71, 31))
        self.buttonBoxCancel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonBoxCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBoxCancel.setObjectName("buttonBoxCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tiplineedit, self.tportlineedit)
        Dialog.setTabOrder(self.tportlineedit, self.buttonBoxOk)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TCP Connection"))
        self.label.setText(_translate("Dialog", "Server IP"))
        self.label_2.setText(_translate("Dialog", "Port"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


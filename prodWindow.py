# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(615, 447)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.textTitle = QtWidgets.QTextEdit(self.centralwidget)
        self.textTitle.setGeometry(QtCore.QRect(90, 20, 131, 31))
        self.textTitle.setObjectName("textTitle")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_7.setObjectName("label_7")
        self.butSave = QtWidgets.QPushButton(self.centralwidget)
        self.butSave.setGeometry(QtCore.QRect(10, 400, 131, 31))
        self.butSave.setObjectName("butSave")
        self.butUndo = QtWidgets.QPushButton(self.centralwidget)
        self.butUndo.setGeometry(QtCore.QRect(240, 400, 131, 31))
        self.butUndo.setObjectName("butUndo")
        self.butDel = QtWidgets.QPushButton(self.centralwidget)
        self.butDel.setGeometry(QtCore.QRect(460, 400, 131, 31))
        self.butDel.setObjectName("butDel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 20, 61, 16))
        self.label_8.setObjectName("label_8")
        self.cboxSupp = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSupp.setGeometry(QtCore.QRect(400, 20, 171, 22))
        self.cboxSupp.setObjectName("cboxSupp")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 120, 91, 16))
        self.label_9.setObjectName("label_9")
        self.listWidgetReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetReserv.setGeometry(QtCore.QRect(310, 150, 221, 192))
        self.listWidgetReserv.setObjectName("listWidgetReserv")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_10.setObjectName("label_10")
        self.listWidgetMeal = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetMeal.setGeometry(QtCore.QRect(20, 150, 221, 192))
        self.listWidgetMeal.setObjectName("listWidgetMeal")
        self.sboxPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sboxPrice.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.sboxPrice.setObjectName("sboxPrice")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "MainWindow"))
        self.label.setText(_translate("EmployeeWindow", "Title"))
        self.label_7.setText(_translate("EmployeeWindow", "Price"))
        self.butSave.setText(_translate("EmployeeWindow", "Save"))
        self.butUndo.setText(_translate("EmployeeWindow", "Undo all"))
        self.butDel.setText(_translate("EmployeeWindow", "Delete"))
        self.label_8.setText(_translate("EmployeeWindow", "Supplier"))
        self.label_9.setText(_translate("EmployeeWindow", "Reservations"))
        self.label_10.setText(_translate("EmployeeWindow", "Meals"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeWindow = QtWidgets.QMainWindow()
    ui = Ui_EmployeeWindow()
    ui.setupUi(EmployeeWindow)
    EmployeeWindow.show()
    sys.exit(app.exec_())

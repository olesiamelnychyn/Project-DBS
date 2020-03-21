# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from GUI import *


class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow, id_emp=0):
        print("IDDDDD ", id_emp)
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(640, 447)

        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName("label_2")

        # Check Box Male/Female ----------------------------------------------------------
        self.rbtnM = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnM.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.rbtnM.setObjectName("rbtnM")
        self.rbtnF = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnF.setGeometry(QtCore.QRect(120, 100, 82, 17))
        self.rbtnF.setObjectName("rbtnF")

        # Text Box First/Last Names ----------------------------------------------------------
        self.textFN = QtWidgets.QTextEdit(self.centralwidget)
        self.textFN.setGeometry(QtCore.QRect(90, 20, 131, 31))
        self.textFN.setObjectName("textFN")
        self.textLN = QtWidgets.QTextEdit(self.centralwidget)
        self.textLN.setGeometry(QtCore.QRect(90, 60, 131, 31))
        self.textLN.setObjectName("textLN")

        # Text Box Birthdate ----------------------------------------------------------
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(90, 130, 131, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_5.setObjectName("label_5")

        # Text Box Phone ----------------------------------------------------------
        self.textPhone = QtWidgets.QTextEdit(self.centralwidget)
        self.textPhone.setGeometry(QtCore.QRect(90, 170, 131, 31))
        self.textPhone.setObjectName("textPhone")

        #Text box E-mail ----------------------------------------------------------
        self.textEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.textEmail.setGeometry(QtCore.QRect(90, 210, 131, 31))
        self.textEmail.setObjectName("textEmail")

        #Text Box Position ----------------------------------------------------------
        self.textPosition = QtWidgets.QTextEdit(self.centralwidget)
        self.textPosition.setGeometry(QtCore.QRect(90, 270, 131, 31))
        self.textPosition.setObjectName("textPosition")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 320, 61, 16))
        self.label_7.setObjectName("label_7")

        self.butSave = QtWidgets.QPushButton(self.centralwidget)
        self.butSave.setGeometry(QtCore.QRect(10, 400, 131, 31))
        self.butSave.setObjectName("butSave")
        self.butUndo = QtWidgets.QPushButton(self.centralwidget)
        self.butUndo.setGeometry(QtCore.QRect(210, 400, 131, 31))
        self.butUndo.setObjectName("butUndo")
        self.butDel = QtWidgets.QPushButton(self.centralwidget)
        self.butDel.setGeometry(QtCore.QRect(460, 400, 131, 31))
        self.butDel.setObjectName("butDel")

        self.sboxWage = QtWidgets.QSpinBox(self.centralwidget)
        self.sboxWage.setGeometry(QtCore.QRect(90, 310, 131, 31))
        self.sboxWage.setObjectName("sboxWage")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 20, 61, 16))
        self.label_8.setObjectName("label_8")

        self.cboxRest = QtWidgets.QComboBox(self.centralwidget)
        self.cboxRest.setGeometry(QtCore.QRect(390, 20, 171, 22))
        self.cboxRest.setObjectName("cboxRest")

        self.tableReserv = QtWidgets.QTableWidget(self.centralwidget)
        self.tableReserv.setGeometry(QtCore.QRect(290, 110, 301, 251))
        self.tableReserv.setObjectName("tableReserv")
        self.tableReserv.setColumnCount(0)
        self.tableReserv.setRowCount(0)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 80, 91, 16))
        self.label_9.setObjectName("label_9")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)

        if(id_emp != 0):
            mycursor.execute("select * from employee where id='"+str(id_emp)+"'; ")
            res=getresult(mycursor)[0]
            print(res)
            self.textFN.setText(str(res[2]))
            self.textLN.setText(str(res[3]))
            if(res[4] == 'M'):
                self.rbtnM.Check = True
            else:
                self.rbtnF.Check = True

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "MainWindow"))
        self.label.setText(_translate("EmployeeWindow", "First name"))
        self.label_2.setText(_translate("EmployeeWindow", "Last name"))
        self.rbtnM.setText(_translate("EmployeeWindow", "Male"))
        self.rbtnF.setText(_translate("EmployeeWindow", "Female"))
        self.label_3.setText(_translate("EmployeeWindow", "Birthday"))
        self.label_4.setText(_translate("EmployeeWindow", "Phone"))
        self.label_5.setText(_translate("EmployeeWindow", "E-mail"))
        self.label_6.setText(_translate("EmployeeWindow", "Position"))
        self.label_7.setText(_translate("EmployeeWindow", "Wage"))
        self.butSave.setText(_translate("EmployeeWindow", "Save"))
        self.butUndo.setText(_translate("EmployeeWindow", "Undo all"))
        self.butDel.setText(_translate("EmployeeWindow", "Delete"))
        self.label_8.setText(_translate("EmployeeWindow", "Restaurant"))
        self.label_9.setText(_translate("EmployeeWindow", "Reservations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeWindow = QtWidgets.QMainWindow()
    ui = Ui_EmployeeWindow()
    ui.setupUi(EmployeeWindow)
    EmployeeWindow.show()
    sys.exit(app.exec_())

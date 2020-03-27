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
        self.id_emp = id_emp
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
        self.sboxWage.setMaximum(400000)
        self.sboxWage.setSingleStep(100)
        self.sboxWage.setObjectName("sboxWage")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 20, 61, 16))
        self.label_8.setObjectName("label_8")

        self.cboxRest = QtWidgets.QComboBox(self.centralwidget)
        self.cboxRest.setGeometry(QtCore.QRect(390, 20, 191, 22))
        self.cboxRest.setObjectName("cboxRest")

        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(290, 110, 301, 251))
        self.listView.setObjectName("listView")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 80, 91, 16))
        self.label_9.setObjectName("label_9")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)
        self.Fill_employee()
        self.butUndo.clicked.connect(self.Fill_employee)
        # self.butSave.clicked.connect(self.Save_employee)
        
        self.cboxRest.currentTextChanged.connect(self.Change_reservation)
        if(id_emp == 0):
            mycursor.execute("select r.capacity, zc.code, zc.state, r.id from zip zc join restaurant r on r.zip=zc.code ")
            res3=getresult(mycursor)
            print(res3)
            for x in res3:
                item = "Capacity: "+str(x[0])+", "+x[1] +", "+ x[2] +", "+str(x[3])
                self.cboxRest.addItem(item)

    def Change_reservation(self, id_emp=1):
        if(self.cboxRest.count() > 0):
            rest_id = str(self.cboxRest.currentText()).split(',')[3]
            self.listView.clear()
            print("right there")
            mycursor.execute("select reservation.id, reservation.date_start, reservation.date_end, reservation.visitors FROM (reservation join emp_reserv on (reservation.id = emp_reserv.reserv_id and emp_reserv.emp_id = "+str(self.id_emp)+")) where reservation.rest_id = "+rest_id)
            res3=getresult(mycursor)
            print(res3)
            for x in res3:
                self.listView.addItem(str(x[0])+": "+str(x[1])+"-"+str(x[2])+", vis: "+str(x[3]))
        
    def Save_employee(self):
        if(self.textFN.toPlainText() != "" and self.textLN.toPlainText() != "" and (self.rbtnF.isChecked() or self.rbtnM.isChecked())
            and self.dateEdit.text() != "" and self.textPhone.toPlainText() != "" and self.textEmail.toPlainText() != ""
            and self.textPosition.toPlainText() != "" and self.sboxWage.text() != ""):
            m = ""
            if(self.rbtnM.isChecked()):
                m = "M" 
            else:
                m = "W"
            rest_id = str(self.cboxRest.currentText()).split(',')[3]
            print(self.dateEdit.text())
            if(self.id_emp != 0):
                mycursor.execute("update employee set "+
                "rest_id = "+rest_id+
                ", first_name =\'"+self.textFN.toPlainText()+
                "\', last_name=\'"+self.textLN.toPlainText()+
                "\', gender= \'"+m+
                "\', birthdate=\'"+str(self.dateEdit.text()).split('.')[2]+"-"+str(self.dateEdit.text()).split('.')[1]+"-"+str(self.dateEdit.text()).split('.')[0]+
                "\', phone=\'"+self.textPhone.toPlainText()+
                "\', e_mail=\'"+self.textEmail.toPlainText()+
                "\', position=\'"+self.textPosition.toPlainText()+
                "\', wage="+str(self.sboxWage.text())+
                " where id="+str(self.id_emp))
                printresult(mycursor)
            else:
                print("add new")
                mycursor.execute("select MAX(id) as id from employee")
                res=getresult(mycursor)[0]
                self.id_emp = int(res[0]) + 1
                sqlinsert = "insert into employee (id, rest_id, first_name, last_name, gender, birthdate, phone, e_mail, position, wage) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = [(self.id_emp, rest_id, self.textFN.toPlainText(), self.textLN.toPlainText(), m, self.dateEdit.text(), self.textPhone.toPlainText(), self.textEmail.toPlainText(), self.textPosition.toPlainText(), str(self.sboxWage.text()))]
                mycursor.executemany(sqlinsert,values)
                printresult(mycursor)
            mydb.commit()

    def Fill_employee(self):
        if(self.id_emp != 0):
            if(self.cboxRest.count() > 0):
                self.cboxRest.clear()
            mycursor.execute("select * from employee where id='"+str(self.id_emp)+"'; ")
            res=getresult(mycursor)[0]
            print(res)
            self.textFN.setText(str(res[2]))
            self.textLN.setText(str(res[3]))
            if(res[4] == 'M'):
                self.rbtnM.setChecked(True)
            else:
                self.rbtnF.setChecked(True)
            date_of_birth = str(res[5]).split("-")
            self.dateEdit.setDate(QtCore.QDate(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2])))
            self.textPhone.setText(str(res[6]))
            self.textEmail.setText(str(res[7]))
            self.textPosition.setText(str(res[8]))
            self.sboxWage.setValue(int(res[9]))
            mycursor.execute("select r.capacity, zc.code, zc.state, r.id from zip zc join restaurant r on r.zip=zc.code where r.id="+str(res[1]))
            res2=getresult(mycursor)[0]
            self.cboxRest.addItem("Capacity: "+str(res2[0])+", "+res2[1]+", "+res2[2]+", "+str(res2[3]))
            mycursor.execute("select r.capacity, zc.code, zc.state, r.id from zip zc join restaurant r on r.zip=zc.code where r.id!="+str(res[1]))
            for x in mycursor:
                item = "Capacity: "+str(x[0])+", "+x[1]+", "+x[2]+", "+str(x[3])
                self.cboxRest.addItem(item)
            if(self.id_emp!=0):
                mycursor.execute("select reservation.id, reservation.date_start, reservation.date_end, reservation.visitors FROM (reservation join emp_reserv on (reservation.id = emp_reserv.reserv_id and emp_reserv.emp_id = "+str(self.id_emp)+")) where reservation.rest_id = "+str(res[1]))
                res3=getresult(mycursor)
                print(res3)
                self.listView.clear()
                for x in res3:
                    self.listView.addItem(str(x[0])+": "+str(x[1])+"-"+str(x[2])+", vis: "+str(x[3]))
                

        else:
            self.textFN.clear()
            self.textLN.clear()
            self.dateEdit.clear()
            self.textPhone.clear()
            self.textEmail.clear()
            self.textPosition.clear()
            self.sboxWage.clear()

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

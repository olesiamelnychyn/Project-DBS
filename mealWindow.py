# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mealWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import datetime

class UiMealWindow(object):
    def setupUi(self, EmployeeWindow, id_meal=2):
        self.id=id_meal
        print(self.id)
        
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(615, 447)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.textFN = QtWidgets.QTextEdit(self.centralwidget)
        self.textFN.setGeometry(QtCore.QRect(90, 20, 131, 31))
        self.textFN.setObjectName("textFN")
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
        self.label_8.setGeometry(QtCore.QRect(320, 20, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 210, 91, 16))
        self.label_9.setObjectName("label_9")
        self.listWidgetReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetReserv.setGeometry(QtCore.QRect(320, 240, 221, 141))
        self.listWidgetReserv.setObjectName("listWidgetReserv")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 91, 16))
        self.label_10.setObjectName("label_10")
        self.listWidgetProd = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetProd.setGeometry(QtCore.QRect(20, 240, 221, 141))
        self.listWidgetProd.setObjectName("listWidgetProd")
        self.sboxPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sboxPrice.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.sboxPrice.setObjectName("sboxPrice")
        self.sboxTime = QtWidgets.QSpinBox(self.centralwidget)
        self.sboxTime.setGeometry(QtCore.QRect(90, 120, 131, 31))
        self.sboxTime.setObjectName("sboxTime")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.label_11.setObjectName("label_11")
        self.listWidgetRest = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetRest.setGeometry(QtCore.QRect(320, 50, 221, 141))
        self.listWidgetRest.setObjectName("listWidgetRest")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)
        self.fill()
        self.butUndo.clicked.connect(self.fill)
        self.butSave.clicked.connect(self.changes)

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "MainWindow"))
        self.label.setText(_translate("EmployeeWindow", "Title"))
        self.label_7.setText(_translate("EmployeeWindow", "Price"))
        self.butSave.setText(_translate("EmployeeWindow", "Save"))
        self.butUndo.setText(_translate("EmployeeWindow", "Undo all"))
        self.butDel.setText(_translate("EmployeeWindow", "Delete"))
        self.label_8.setText(_translate("EmployeeWindow", "Restaurants"))
        self.label_9.setText(_translate("EmployeeWindow", "Reservations"))
        self.label_10.setText(_translate("EmployeeWindow", "Products"))
        self.label_11.setText(_translate("EmployeeWindow", "Time"))

    def fill(self):

        res=getresult(mycursor.execute("select * from meal where id="+str(self.id)))[0]
        self.textFN.clear()
        self.textFN.insertPlainText(res[1])
        self.sboxPrice.setValue(res[2])
        self.sboxTime.setValue((res[3]).total_seconds())
        res=getresult(mycursor.execute("select p.title, p.price, s.title from product p join meal_product m on m.prod_id=p.id join supplier s on p.supp_id=s.id where m.meal_id="+str(self.id)))
        print(res)
        self.listWidgetProd.clear()
        for result in res:
            self.listWidgetProd.addItem(result[0]+", price: "+str(result[1])+", supplier: "+result[2])
        res=getresult(mycursor.execute("select r.capacity, zc.state from restaurant r join meal_rest m on m.rest_id=r.id join zip zc on r.zip=zc.code where m.meal_id="+str(self.id)))
        self.listWidgetRest.clear()
        for result in res:
            self.listWidgetRest.addItem("Capacity: "+str(result[0])+", "+result[1])
        # print(res)
        res=getresult(mycursor.execute("select DATE_FORMAT(r.date_start, \"%H:%i\"), DATE_FORMAT(r.date_end, \"%H:%i\"), r.visitors from reservation r join meal_reserv m on m.reserv_id=r.id where m.meal_id="+str(self.id)))
        print(res)
        self.listWidgetReserv.clear()
        for result in res:
            self.listWidgetReserv.addItem("Visitors: "+str(result[2])+", start: "+str(result[0])+", end: "+str(result[1]))

    def changes(self):
        if(self.textFN.toPlainText()==""):
            self.textFN.insertPlainText("Enter title!")
            return
        if(self.id!=0):
            mycursor.execute("update meal set title=\'"+self.textFN.toPlainText()+"\', price=\'"+self.sboxPrice.text()+"\', prep_time=\'"+self.sboxTime.text()+"\' where id="+str(self.id))
        else:
            mycursor.execute("insert into meal (title, price, prep_time) values(\'"+self.textFN.toPlainText()+"\', "+self.sboxPrice.text()+", \'00.00."+self.sboxTime.text()+"\' where id="+str(self.id)) 
        print(getresult(mycursor.execute("select * from meal where id="+str(self.id)))[0])
        mydb.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeWindow = QtWidgets.QMainWindow()
    ui = UiMealWindow()
    ui.setupUi(EmployeeWindow)
    EmployeeWindow.show()
    sys.exit(app.exec_())

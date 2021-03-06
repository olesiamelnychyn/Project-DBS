# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mealWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SQLfiles.main import *
import datetime

class UiMealWindow(object):
    def setupUi(self, EmployeeWindow, id_meal=0):
        self.id=id_meal
        print(self.id)
        
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(615, 447)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.textTitle = QtWidgets.QTextEdit(self.centralwidget)
        self.textTitle.setGeometry(QtCore.QRect(80, 20, 131, 31))
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
        self.label_8.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 210, 91, 16))
        self.label_9.setObjectName("label_9")
        self.listWidgetReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetReserv.setGeometry(QtCore.QRect(330, 240, 221, 141))
        self.listWidgetReserv.setObjectName("listWidgetReserv")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 40, 51, 16))
        self.label_10.setObjectName("label_10")
        self.listWidgetProd = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetProd.setGeometry(QtCore.QRect(370, 30, 221, 141))
        self.listWidgetProd.setObjectName("listWidgetProd")
        self.sboxPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sboxPrice.setGeometry(QtCore.QRect(80, 70, 101, 31))
        self.sboxPrice.setObjectName("sboxPrice")
        self.sboxTime = QtWidgets.QSpinBox(self.centralwidget)
        self.sboxTime.setGeometry(QtCore.QRect(80, 120, 101, 31))
        self.sboxTime.setObjectName("sboxTime")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 51, 16))
        self.label_11.setObjectName("label_11")
        self.listWidgetRest = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetRest.setGeometry(QtCore.QRect(20, 240, 221, 141))
        self.listWidgetRest.setObjectName("listWidgetRest")
        self.butAddProd = QtWidgets.QPushButton(self.centralwidget)
        self.butAddProd.setGeometry(QtCore.QRect(380, 180, 61, 23))
        self.butAddProd.setObjectName("butAddProd")
        self.butDelProd = QtWidgets.QPushButton(self.centralwidget)
        self.butDelProd.setGeometry(QtCore.QRect(520, 180, 61, 23))
        self.butDelProd.setObjectName("butDelProd")
        self.textProdID = QtWidgets.QTextEdit(self.centralwidget)
        self.textProdID.setGeometry(QtCore.QRect(230, 70, 81, 31))
        self.textProdID.setObjectName("textProdID")
        self.listWProd = QtWidgets.QListWidget(self.centralwidget)
        self.listWProd.setGeometry(QtCore.QRect(230, 110, 131, 61))
        self.listWProd.setObjectName("listWProd")
        self.butProdS = QtWidgets.QPushButton(self.centralwidget)
        self.butProdS.setGeometry(QtCore.QRect(330, 70, 31, 31))
        self.butProdS.setText("")
        self.butProdS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butProdS.setObjectName("butProdS")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)
        self.fill()
        self.butUndo.clicked.connect(self.fill)
        self.butProdS.clicked.connect(self.prod_search)
        self.butAddProd.clicked.connect(self.add_product)
        self.butDelProd.clicked.connect(self.del_product)

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
        self.butAddProd.setText(_translate("EmployeeWindow", "Add"))
        self.butDelProd.setText(_translate("EmployeeWindow", "Delete"))

    def fill(self):
        if(self.id!=0):
            res=getresult(mycursor.execute("select id, title, price, DATE_FORMAT(prep_time, \"%i\")  from meal where id="+str(self.id)))[0]
            self.textTitle.clear()
            print(res[3])
            self.textTitle.insertPlainText(res[1])
            self.sboxPrice.setValue(res[2])
            self.sboxTime.setValue(int(res[3]))
            res=getresult(mycursor.execute("select p.title, p.price, s.title, p.id from product p join meal_product m on m.prod_id=p.id join supplier s on p.supp_id=s.id where m.meal_id="+str(self.id)))
            print(res)
            self.listWidgetProd.clear()
            for result in res:
                self.listWidgetProd.addItem("ID: "+str(result[3])+", "+result[0]+", price: "+str(result[1])+", supplier: "+result[2])
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
        if(self.textTitle.toPlainText()==""):
            self.textTitle.insertPlainText("Enter title!")
            return
        if(self.id!=0):
            mycursor.execute("update meal set title=\'"+self.textTitle.toPlainText()+"\', price=\'"+self.sboxPrice.text()+"\', prep_time=time(\"00:"+self.sboxTime.text()+":00\") where id="+str(self.id))
        else:
            insert="insert into meal (title, price, prep_time) values(\'"+self.textTitle.toPlainText()+"\', "+self.sboxPrice.text().replace(",", ".")+", time(\"00:"+self.sboxTime.text()+":00\"))"
            print(insert)
            mycursor.execute(insert) 
            self.id=getresult(mycursor.execute("Select max(id) from meal"))[0][0]
            print(self.id)
        print(getresult(mycursor.execute("select * from meal where id="+str(self.id)))[0])
        mydb.commit()

    def prod_search(self):
        if(self.textProdID.toPlainText()!=''):
            result=getresult(mycursor.execute("select id, title, price from product where id="+self.textProdID.toPlainText()))[0]
            print(result)
            self.listWProd.clear()
            self.listWProd.addItem(result[1]+", price: "+str(result[2]))
    
    def add_product(self):
        if(self.id==0):
            self.textProdID.insertPlainText("Create meal first!")
            return
        if(self.textProdID.toPlainText()!='' ):
            print(len(getresult(mycursor.execute("select * from meal_product where meal_id="+str(self.id)+" and prod_id="+self.textProdID.toPlainText()))))
            if(len(getresult(mycursor.execute("select * from meal_product where meal_id="+str(self.id)+" and prod_id="+self.textProdID.toPlainText())))==0):
                mycursor.execute("insert into meal_product (meal_id, prod_id) values("+str(self.id)+", "+self.textProdID.toPlainText()+")")
                # mydb.commit()
                self.fill()

    def del_product(self):
        # print(self.listWidgetProd.selectedItems()[0].text())
        if(len(self.listWidgetProd.selectedItems())!=0):
            # print("here")
            x=self.listWidgetProd.selectedItems()[0].text().split(",")[0].replace("ID: ", "")
            mycursor.execute("delete from meal_product where prod_id="+x)
            # mydb.commit()
            print(x)
            self.listWidgetProd.clear()
            self.fill()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeWindow = QtWidgets.QMainWindow()
    ui = UiMealWindow()
    ui.setupUi(EmployeeWindow)
    EmployeeWindow.show()
    sys.exit(app.exec_())

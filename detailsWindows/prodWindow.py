# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SQLfiles.main import *
from GUI import *


class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow, id_prod = 0):
        self.id = id_prod
        ProductWindow.setObjectName("ProductWindow")
        ProductWindow.resize(615, 447)
        self.centralwidget = QtWidgets.QWidget(ProductWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.textTitle = QtWidgets.QTextEdit(self.centralwidget)
        self.textTitle.setGeometry(QtCore.QRect(90, 20, 131, 31))
        self.textTitle.setObjectName("textTitle")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_7.setObjectName("label_7")

        # Buttons
        self.butSave = QtWidgets.QPushButton(self.centralwidget)
        self.butSave.setGeometry(QtCore.QRect(10, 400, 131, 31))
        self.butSave.setObjectName("butSave")
        self.butUndo = QtWidgets.QPushButton(self.centralwidget)
        self.butUndo.setGeometry(QtCore.QRect(240, 400, 131, 31))
        self.butUndo.setObjectName("butUndo")
        self.butDel = QtWidgets.QPushButton(self.centralwidget)
        self.butDel.setGeometry(QtCore.QRect(460, 400, 131, 31))
        self.butDel.setObjectName("butDel")

        # Supplier
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 20, 61, 16))
        self.label_8.setObjectName("label_8")
        self.cboxSupp = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSupp.setGeometry(QtCore.QRect(390, 20, 191, 22))
        self.cboxSupp.setObjectName("cboxSupp")
        if(self.id == 0):
            mycursor.execute("select s.title, s.phone, s.id from supplier s ")
            res=getresult(mycursor)
            print(res)
            for x in res:
                item = x[0]+", "+x[1] +", "+str(x[2])
                self.cboxSupp.addItem(item)

        # list of Reservations
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 120, 91, 16))
        self.label_9.setObjectName("label_9")
        self.listWidgetReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetReserv.setGeometry(QtCore.QRect(310, 150, 221, 192))
        self.listWidgetReserv.setObjectName("listWidgetReserv")

        # list of Meals
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_10.setObjectName("label_10")
        self.listWidgetMeal = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetMeal.setGeometry(QtCore.QRect(20, 150, 221, 192))
        self.listWidgetMeal.setObjectName("listWidgetMeal")

        self.sboxPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sboxPrice.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.sboxPrice.setObjectName("sboxPrice")
        ProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductWindow)

        self.fill_product()
        self.butUndo.clicked.connect(self.fill_product)

    def retranslateUi(self, ProductWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductWindow.setWindowTitle(_translate("ProductWindow", "MainWindow"))
        self.label.setText(_translate("ProductWindow", "Title"))
        self.label_7.setText(_translate("ProductWindow", "Price"))
        self.butSave.setText(_translate("ProductWindow", "Save"))
        self.butUndo.setText(_translate("ProductWindow", "Undo all"))
        self.butDel.setText(_translate("ProductWindow", "Delete"))
        self.label_8.setText(_translate("ProductWindow", "Supplier"))
        self.label_9.setText(_translate("ProductWindow", "Reservations"))
        self.label_10.setText(_translate("ProductWindow", "Meals"))

    def save_clicked(self):
        if(self.textTitle.toPlainText()==""):
            self.textTitle.insertPlainText("Enter title!")
            return
        if(self.sboxPrice.value() == 0):
            return
        if(self.id == 0):
            print("add new")
            sqlinsert = "insert into product (title, price, supp_id) values(%s,%s,%s)"
            values = [(self.textTitle.toPlainText(), self.sboxPrice.value(), str(self.cboxSupp.currentText()).split(',')[2])]
            mycursor.executemany(sqlinsert,values)
            printresult(mycursor)
        else:
            mycursor.execute("update product set "+
                "supp_id = "+str(self.cboxSupp.currentText()).split(',')[2]+
                ", title =\'"+self.textTitle.toPlainText()+
                "\', price="+str(self.sboxPrice.value())+
                " where id="+str(self.id))
            printresult(mycursor)
        mydb.commit()

    def fill_product(self):
        if(self.id != 0):
            mycursor.execute("select * from product where id='"+str(self.id)+"'; ")
            res=getresult(mycursor)[0]
            print(res)
            self.textTitle.setText(str(res[1]))
            self.sboxPrice.setValue(res[2])

            mycursor.execute("select s.title, s.phone, s.id from supplier s join product p on p.supp_id = s.id where p.id = \'" + str(self.id) + "\';")
            res2=getresult(mycursor)[0]
            self.cboxSupp.clear()
            self.cboxSupp.addItem(res2[0]+", "+res2[1] +", "+str(res2[2]))
            mycursor.execute("select s.title, s.phone, s.id from supplier s where s.id != \'" + str(res2[2]) + "\';")
            res2=getresult(mycursor)
            print("supplier")
            print(res2)
            for x in res2:
                item = x[0]+", "+x[1] +", "+str(x[2])
                self.cboxSupp.addItem(item)

            mycursor.execute("select meal.title, meal.price, meal.prep_time FROM (meal join meal_product on meal.id = meal_product.meal_id) where meal_product.prod_id = "+str(self.id))
            res3=getresult(mycursor)
            print(res3)
            self.listWidgetMeal.clear()
            for x in res3:
                self.listWidgetMeal.addItem(str(x[0])+" : "+str(x[1])+"$ - time: "+str(x[2]))

            mycursor.execute("select reservation.id, reservation.date_start, reservation.date_end, reservation.visitors FROM (reservation join meal_reserv on reservation.id = meal_reserv.reserv_id join meal on meal.id = meal_reserv.meal_id join meal_product on meal.id = meal_product.meal_id ) where meal_product.prod_id = "+str(self.id))
            res3=getresult(mycursor)
            print(res3)
            self.listWidgetReserv.clear()
            for x in res3:
                item = str(x[0])+": "+str(x[1])+"-"+str(x[2])+", vis: "+str(x[3])
                if(self.Not_exist(item) == True):
                    self.listWidgetReserv.addItem(item)

    def Not_exist(self, item):
        for i in range(self.listWidgetReserv.count()):
            if(self.listWidgetReserv.item(i).text() == item):
                return False
        return True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductWindow()
    ui.setupUi(ProductWindow)
    ProductWindow.show()
    sys.exit(app.exec_())

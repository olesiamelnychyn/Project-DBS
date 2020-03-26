# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchMealWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import GUI
from main import *


class Ui_SearchMeal(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 491)
        SearchWindow.setStyleSheet("background:#fafafe;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setObjectName("textSearch")
        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(460, 450, 161, 31))
        self.butSearch.setObjectName("butSearch")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 150, 121, 16))
        self.label_3.setObjectName("label_3")
        self.textProd = QtWidgets.QTextEdit(self.centralwidget)
        self.textProd.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textProd.setObjectName("textProd")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 141, 16))
        self.label_4.setObjectName("label_4")
        self.butProdS = QtWidgets.QPushButton(self.centralwidget)
        self.butProdS.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.butProdS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butProdS.setText("")
        self.butProdS.setObjectName("butProdS")
        self.listViewProd = QtWidgets.QListWidget(self.centralwidget)
        self.listViewProd.setGeometry(QtCore.QRect(460, 70, 161, 71))
        self.listViewProd.setObjectName("listViewProd")
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 450, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 450, 171, 31))
        self.butAdd.setObjectName("butAdd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 170, 41, 27))
        self.label.setObjectName("label")
        self.textFromPrice = QtWidgets.QTextEdit(self.centralwidget)
        self.textFromPrice.setGeometry(QtCore.QRect(510, 170, 101, 31))
        self.textFromPrice.setObjectName("textFromPrice")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 210, 31, 21))
        self.label_2.setObjectName("label_2")
        self.textToPrice = QtWidgets.QTextEdit(self.centralwidget)
        self.textToPrice.setGeometry(QtCore.QRect(510, 210, 101, 31))
        self.textToPrice.setObjectName("textToPrice")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 421, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Preraration time"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 130)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(0)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 360, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Choose order")
        self.comboBox.addItem("Title")
        self.comboBox.addItem("Price")
        self.comboBox.addItem("Preparation time")

        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(570, 360, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")
        
        self.cboxGroup = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGroup.setGeometry(QtCore.QRect(460, 400, 161, 22))
        self.cboxGroup.setObjectName("cboxGroup")
        self.cboxGroup.addItem("Choose group by")
        self.cboxGroup.addItem("Restaurant")
        self.cboxGroup.addItem("Reservation")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 270, 41, 27))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 250, 121, 16))
        self.label_6.setObjectName("label_6")
        self.textToTime = QtWidgets.QTextEdit(self.centralwidget)
        self.textToTime.setGeometry(QtCore.QRect(510, 310, 101, 31))
        self.textToTime.setObjectName("textToTime")
        self.textFromTime = QtWidgets.QTextEdit(self.centralwidget)
        self.textFromTime.setGeometry(QtCore.QRect(510, 270, 101, 31))
        self.textFromTime.setObjectName("textFromTime")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 310, 31, 21))
        self.label_7.setObjectName("label_7")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

        self.fill()
        self.butSearch.clicked.connect(self.search_meals)
        self.butProdS.clicked.connect(self.search_pro_id)
        self.butDelete.clicked.connect(self.del_meal)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.butSearch.setText(_translate("SearchWindow", "Search"))
        self.label_3.setText(_translate("SearchWindow", "Choose price range"))
        self.label_4.setText(_translate("SearchWindow", "Enter product code"))
        self.butDelete.setText(_translate("SearchWindow", "Delete"))
        self.butAdd.setText(_translate("SearchWindow", "Add"))
        self.label.setText(_translate("SearchWindow", "from"))
        self.label_2.setText(_translate("SearchWindow", "to"))
        self.chboxDesc.setText(_translate("SearchWindow", "Desc"))
        self.label_5.setText(_translate("SearchWindow", "from"))
        self.label_6.setText(_translate("SearchWindow", "Choose preparation time"))
        self.label_7.setText(_translate("SearchWindow", "to"))

    def search_pro_id(self):
        self.listViewProd.clear()
        id_prod=self.textProd.toPlainText()
        if(id_prod!=""):
            res=getresult(mycursor.execute("Select p.title, p.price, s.title from product p join supplier s on s.id=p.supp_id where p.id="+id_prod))[0]
            self.listViewProd.addItem(res[0]+", price: "+str(res[1])+", supp: "+str(res[2]))

    def fill(self):
        result=search_meals(False)
        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(str(res[2])))
            self.tableWidget.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))
        
    def search_meals(self):
        args={'title':'',
        'price_from':'',
        'price_to':'',
        'prep_from':'',
        'prep_to':'',
        'product_in':'',
        'order_by':'',
        'group_by':''}
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Preraration time"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        args['title']=self.textSearch.toPlainText()

        if(self.textFromPrice.toPlainText()==""):
            args['price_from']=str(0.0)
        else:
            args['price_from']=self.textFromPrice.toPlainText()

        if(self.textToPrice.toPlainText()==""):
            res=getresult(mycursor.execute("select max(price) from meal"))[0]
            print(res)
            args['price_to']=str(res[0])
        else:
            args['price_to']=self.textToPrice.toPlainText()

        if(self.textFromTime.toPlainText()==""):
            args['prep_from']="00:00:00"
        else: 
            args['prep_from']=self.textFromTime.toPlainText()
        if(self.textToTime.toPlainText()==""):
            res=getresult(mycursor.execute("select max(prep_time) from meal")) [0]
            args['prep_to']="0"+str(res[0])
        else:
            args['prep_to']=self.textToTime.toPlainText()

        args['product_in']=self.textProd.toPlainText()

        if(self.comboBox.currentText()!="Choose order"):
            if(self.comboBox.currentText()=="Preparation time"):
                args['order_by']="prep_time"
            else:
                args['order_by']=self.comboBox.currentText().lower()
            if(self.chboxDesc.isChecked()):
                args['order_by']+=" desc"
        if(self.cboxGroup.currentText()!="Choose group by"):
            args['group_by']=self.cboxGroup.currentText().lower()
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(self.cboxGroup.currentText()))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Sum for all"))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Average"))
        print(args)
        result=search_meals(args)
        print(result)
           
        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            if(self.cboxGroup.currentText()=="Reservation"):
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem("vis: "+str(res[1])+", "+str(res[4])+", "+str(res[5])))
            elif(self.cboxGroup.currentText()=="Restaurant"):
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem("cap: "+str(res[1])+", "+str(res[4])))
            else:
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(str(res[2])))
            self.tableWidget.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))

    def del_meal(self):
        if(len(self.tableWidget.selectionModel().selection().indexes())!=0):
            row=self.tableWidget.selectionModel().selection().indexes()[0].row()
            item_id=self.tableWidget.item(row, 0).text()
            delete_meals(item_id)
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.fill()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchMeal()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

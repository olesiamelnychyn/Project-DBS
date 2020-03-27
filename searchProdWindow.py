# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchProdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
from GUI import *


class Ui_SearchProd(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 491)
        SearchWindow.setStyleSheet("background:#fafafe;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setPlaceholderText("Enter title here...")
        self.textSearch.setObjectName("textSearch")
        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(460, 450, 161, 31))
        self.butSearch.setObjectName("butSearch")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 150, 121, 16))
        self.label_3.setObjectName("label_3")

        # Suppliers
        self.textSupp = QtWidgets.QTextEdit(self.centralwidget)
        self.textSupp.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textSupp.setObjectName("textSupp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 141, 16))
        self.label_4.setObjectName("label_4")
        self.butSuppS = QtWidgets.QPushButton(self.centralwidget)
        self.butSuppS.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.butSuppS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butSuppS.setText("")
        self.butSuppS.setObjectName("butSuppS")
        self.listViewSupp = QtWidgets.QListWidget(self.centralwidget)
        self.listViewSupp.setGeometry(QtCore.QRect(460, 70, 161, 71))
        self.listViewSupp.setObjectName("listViewSupp")

        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 450, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 450, 171, 31))
        self.butAdd.setObjectName("butAdd")

        # Price
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 170, 41, 27))
        self.label.setObjectName("label")
        self.textFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textFrom.setGeometry(QtCore.QRect(510, 170, 101, 31))
        self.textFrom.setObjectName("textFrom")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 210, 31, 21))
        self.label_2.setObjectName("label_2")
        self.textTo = QtWidgets.QTextEdit(self.centralwidget)
        self.textTo.setGeometry(QtCore.QRect(510, 210, 101, 31))
        self.textTo.setObjectName("textTo")

        # Table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 421, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Supplier"))
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setStyleSheet("color: black")

        # Button Home
        self.butHome = QtWidgets.QPushButton(self.centralwidget)
        self.butHome.setGeometry(QtCore.QRect(205, 450, 31, 31))
        self.butHome.setStyleSheet("background-image: url(./img/home.png);")
        self.butHome.setText("")
        self.butHome.setObjectName("butHome")
        
        # Order by
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 260, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Choose order")
        self.comboBox.addItem("Title")
        self.comboBox.addItem("Price")
        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(570, 260, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")

        # Group by
        self.cboxGroup = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGroup.setGeometry(QtCore.QRect(460, 300, 161, 22))
        self.cboxGroup.setObjectName("cboxGroup")
        self.cboxGroup.addItem("Choose group by")
        self.cboxGroup.addItem("Meal")
        self.cboxGroup.addItem("Supplier")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

        self.fill_data()
        self.butSearch.clicked.connect(self.search_products)
        self.butSuppS.clicked.connect(self.butSuppS_clicked)
        self.butDelete.clicked.connect(self.delete_product)

    def fill_data(self):
        mycursor.execute("select * from product")
        result = getresult(mycursor)
        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(res[2])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(res[3])))

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.butSearch.setText(_translate("SearchWindow", "Search"))
        self.label_3.setText(_translate("SearchWindow", "Choose price range"))
        self.label_4.setText(_translate("SearchWindow", "Enter supplier\'s code"))
        self.butDelete.setText(_translate("SearchWindow", "Delete"))
        self.butAdd.setText(_translate("SearchWindow", "Add"))
        self.label.setText(_translate("SearchWindow", "from"))
        self.label_2.setText(_translate("SearchWindow", "to"))
        self.chboxDesc.setText(_translate("SearchWindow", "Desc"))

    def butSuppS_clicked(self):
        self.listViewSupp.clear()
        id_supp = self.textSupp.toPlainText()
        if(id_supp != ""):
            mycursor.execute("select supplier.title, supplier.phone from supplier where supplier.id="+id_supp)
            res = getresult(mycursor)[0]
            self.listViewSupp.addItem(res[0] + ", phone: " + res[1])

    def delete_product(self):
        if(len(self.tableWidget.selectionModel().selection().indexes())!=0):
            row=self.tableWidget.selectionModel().selection().indexes()[0].row()
            item_id=self.tableWidget.item(row, 0).text()
            delete_product(item_id)
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.fill_data()

    def search_products(self):
        args={'title':'',
        'price_from':'',
        'price_to':'',
        'supplier':'',
        'order_by':'',
        'group_by':''}
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Supplier"))
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(3, 120)
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        args['title'] = self.textSearch.toPlainText()

        if(self.textFrom.toPlainText() == ""):
            args['price_from'] = str(0.0)
        else:
            args['price_from'] = self.textFrom.toPlainText()

        if(self.textTo.toPlainText() == ""):
            res=getresult(mycursor.execute("select max(price) from product"))[0]
            print(res)
            args['price_to']=str(res[0])
        else:
            args['price_to']=self.textTo.toPlainText()

        args['supplier']=self.textSupp.toPlainText()

        if(self.comboBox.currentText()!="Choose order"):
            args['order_by']=self.comboBox.currentText().lower()
        if(self.chboxDesc.isChecked()):
            args['order_by']+=" desc"
        if(self.cboxGroup.currentText()!="Choose group by"):
            args['group_by']=self.cboxGroup.currentText().lower()
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(self.cboxGroup.currentText()))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Sum"))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Average"))
            self.tableWidget.setColumnWidth(1, 200)
            self.tableWidget.setColumnWidth(3, 50)
        print(args)
        result=search_products(args)
        print(result)

        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            if(self.cboxGroup.currentText()=="Meal"):
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(str(res[1]) + ": "+ str(res[4]) + "$"))
            elif(self.cboxGroup.currentText()=="Supplier"):
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(str(res[1])))
            else:
                self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(str(res[2])))
            self.tableWidget.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchProd()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

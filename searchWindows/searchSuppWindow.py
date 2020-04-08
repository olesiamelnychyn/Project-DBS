# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchSuppWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SQLfiles.main import *


class Ui_SuppWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 491)
        SearchWindow.setStyleSheet("background: white")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setObjectName("textSearch")
        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(450, 10, 171, 31))
        self.butSearch.setObjectName("butSearch")
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(450, 450, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(450, 410, 171, 31))
        self.butAdd.setObjectName("butAdd")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 421, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Phone"))
        self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("E-mail"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 145)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 135)
        
        # Button Home
        self.butHome = QtWidgets.QPushButton(self.centralwidget)
        self.butHome.setGeometry(QtCore.QRect(450, 170, 31, 31))
        self.butHome.setStyleSheet("background-image: url(./img/home.png);")
        self.butHome.setText("")
        self.butHome.setObjectName("butHome")

        self.textTittle = QtWidgets.QTextEdit(self.centralwidget)
        self.textTittle.setGeometry(QtCore.QRect(520, 50, 104, 31))
        self.textTittle.setObjectName("textTittle")
        self.textTittle.setPlaceholderText("Enter title here...")
        self.textPhone = QtWidgets.QTextEdit(self.centralwidget)
        self.textPhone.setGeometry(QtCore.QRect(520, 90, 104, 31))
        self.textPhone.setObjectName("textPhone")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(520, 130, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 140, 47, 13))
        self.label_3.setObjectName("label_3")
        self.butClear = QtWidgets.QPushButton(self.centralwidget)
        self.butClear.setGeometry(QtCore.QRect(520, 170, 101, 31))
        self.butClear.setObjectName("butClear")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)
        self.fill()
        self.butSearch.clicked.connect(self.search)
        self.butAdd.clicked.connect(self.add)
        self.butClear.clicked.connect(self.clear)
        self.tableWidget.clicked.connect(self.item_supp)
        self.butDelete.clicked.connect(self.delete)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.butSearch.setText(_translate("SearchWindow", "Search"))
        self.butDelete.setText(_translate("SearchWindow", "Delete"))
        self.butAdd.setText(_translate("SearchWindow", "Add"))
        self.label.setText(_translate("SearchWindow", "Tittle"))
        self.label_2.setText(_translate("SearchWindow", "Phone"))
        self.label_3.setText(_translate("SearchWindow", "E-mail"))
        self.butClear.setText(_translate("SearchWindow", "Clear"))

    def search(self):
        args=self.textSearch.toPlainText()
        print(args)
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        result = search_supp(args)
        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
            self.tableWidget.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))


    def fill(self):
        result = search_supp('')
        for res in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableWidget.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableWidget.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
            self.tableWidget.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))

    def add(self):
        title=self.textTittle.toPlainText()
        if(title==''):
            self.textTittle.setText("Enter title!")
            return 
        phone=self.textPhone.toPlainText()
        if(len(phone)!=13):
            self.textPhone.setText("Phone must contain 13 numbers!")
            return
        email=self.textEdit_3.toPlainText()
        if(email==''):
            self.textEdit_3.setText("Enter e-mail!")
            return
        add_supp(title, phone, email)
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.fill()
        self.clear()
    
    def clear(self):
        self.textTittle.setText("")
        self.textPhone.setText("")
        self.textEdit_3.setText("")
    
    def item_supp(self):
        row=self.tableWidget.selectionModel().selection().indexes()[0].row()
        item_id=self.tableWidget.item(row, 0).text()
        print("ID "+item_id)
        mycursor.execute("select * from supplier where id="+item_id)
        result=getresult(mycursor)[0]
        self.textTittle.setText(result[1])
        self.textPhone.setText(result[2])
        self.textEdit_3.setText(result[3])
    
    def delete(self):
        row=self.tableWidget.selectionModel().selection().indexes()[0].row()
        item_id=self.tableWidget.item(row, 0).text()
        print("ID "+item_id)
        mycursor.execute("delete from supplier where id="+item_id)
        mydb.commit()
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.fill()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SuppWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

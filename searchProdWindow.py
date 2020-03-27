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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Title"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setStyleSheet("color: black")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchProd()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

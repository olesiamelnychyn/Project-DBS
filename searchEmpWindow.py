# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchEmpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 447)
        SearchWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setObjectName("textSearch")
        self.textSearch.setPlaceholderText("Enter name or surname here...")

        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(460, 400, 161, 31))
        
        self.butSearch.setObjectName("butSearch")
        self.butSearch.clicked.connect(self.btnSeacrhClick)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 210, 121, 16))
        self.label_3.setObjectName("label_3")
        self.rbtnM = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnM.setGeometry(QtCore.QRect(460, 310, 82, 17))
        self.rbtnM.setObjectName("rbtnM")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 310, 71, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.cboxPos = QtWidgets.QComboBox(self.centralwidget)
        self.cboxPos.setGeometry(QtCore.QRect(460, 330, 161, 21))
        self.cboxPos.setObjectName("cboxPos")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 360, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(580, 360, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")
        self.textRest = QtWidgets.QTextEdit(self.centralwidget)
        self.textRest.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textRest.setObjectName("textRest")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 141, 16))
        self.label_4.setObjectName("label_4")
        self.butRestS = QtWidgets.QPushButton(self.centralwidget)
        self.butRestS.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.butRestS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butRestS.setText("")
        self.butRestS.setObjectName("butRestS")

        # self.model = QStandardItemModel()
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 421, 331))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(4)
        self.tableView.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableView.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("First name"))
        self.tableView.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Last name"))
        self.tableView.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Wage"))
        self.tableView.setColumnWidth(0, 30)
        self.tableView.setColumnWidth(1, 130)
        self.tableView.setColumnWidth(2, 130)
        self.tableView.setColumnWidth(3, 130)
        self.tableView.verticalHeader().hide()
        # self.tableView.setDisabled(True)
        self.tableView.setStyleSheet("color: black")

        # self.tableView.setModel(self.model)

        self.listViewRest = QtWidgets.QListView(self.centralwidget)
        self.listViewRest.setGeometry(QtCore.QRect(460, 70, 161, 31))
        self.listViewRest.setObjectName("listViewRest")
        self.testReserv = QtWidgets.QTextEdit(self.centralwidget)
        self.testReserv.setGeometry(QtCore.QRect(460, 130, 111, 31))
        self.testReserv.setObjectName("testReserv")
        self.butResS = QtWidgets.QPushButton(self.centralwidget)
        self.butResS.setGeometry(QtCore.QRect(590, 130, 31, 31))
        self.butResS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butResS.setText("")
        self.butResS.setObjectName("butResS")
        self.listViewReserv = QtWidgets.QListView(self.centralwidget)
        self.listViewReserv.setGeometry(QtCore.QRect(460, 170, 161, 31))
        self.listViewReserv.setObjectName("listViewReserv")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 110, 111, 16))
        self.label_5.setObjectName("label_5")
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 400, 171, 31))

        self.butDelete.setObjectName("butDelete")
        self.butDelete.clicked.connect(self.btnDeleteClick)

        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 400, 171, 31))
        self.butAdd.setObjectName("butAdd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 230, 41, 27))
        self.label.setObjectName("label")
        self.textFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textFrom.setGeometry(QtCore.QRect(520, 230, 101, 31))
        self.textFrom.setObjectName("textFrom")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 270, 31, 21))
        self.label_2.setObjectName("label_2")
        self.textTo = QtWidgets.QTextEdit(self.centralwidget)
        self.textTo.setGeometry(QtCore.QRect(520, 270, 101, 31))
        self.textTo.setObjectName("textTo")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.butSearch.setText(_translate("SearchWindow", "Search"))
        self.label_3.setText(_translate("SearchWindow", "Choose wage range"))
        self.rbtnM.setText(_translate("SearchWindow", "Male"))
        self.radioButton_2.setText(_translate("SearchWindow", "Female"))
        self.label_4.setText(_translate("SearchWindow", "Enter restaurant code"))
        self.label_5.setText(_translate("SearchWindow", "Enter reservation code"))
        self.butDelete.setText(_translate("SearchWindow", "Delete"))
        self.butAdd.setText(_translate("SearchWindow", "Add"))
        self.label.setText(_translate("SearchWindow", "from"))
        self.label_2.setText(_translate("SearchWindow", "to"))
        self.chboxDesc.setText(_translate("SearchWindow", "Desc"))

    def btnSeacrhClick(self):
        while (self.tableView.rowCount() > 0):
            self.tableView.removeRow(0)

        if(self.textSearch.toPlainText()!=""):
            mycursor.execute("select id, first_name, last_name, wage from employee where first_name like \'"+self.textSearch.toPlainText()+"%\' or last_name like \'"+self.textSearch.toPlainText()+"%\' ")
            result=[]
            for x in mycursor:
                result.append(x)
            self.textSearch.clear()
        else:
            result = search_all("employees")
        print(result)
        for res in result:
            rowPosition = self.tableView.rowCount()
            self.tableView.insertRow(rowPosition)
            self.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableView.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableView.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
            self.tableView.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))


    def btnDeleteClick(self):
        row=self.tableView.selectionModel().selection().indexes()[0].row()
        item_id=self.tableView.item(row, 0).text()
        delete_employee("employee", item_id)
        while (self.tableView.rowCount() > 0):
            self.tableView.removeRow(0)
        result = search_all("employees")
        for res in result:
            rowPosition = self.tableView.rowCount()
            self.tableView.insertRow(rowPosition)
            self.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableView.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
            self.tableView.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
            self.tableView.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))

                
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchEmpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from QtGui import *
# from QtCore import *
from main import *


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 447)
        SearchWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Text Edit Search ----------------------------------------------------------
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setObjectName("textSearch")
        self.textSearch.setPlaceholderText("Enter name or surname here...")

        # Button Search ----------------------------------------------------------
        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(460, 400, 161, 31))
        self.butSearch.setObjectName("butSearch")
        self.butSearch.clicked.connect(self.btnSeacrhClick)

        # Labels ----------------------------------------------------------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 210, 121, 16))
        self.label_3.setObjectName("label_3")

        # Radio Buttons Male/Female ----------------------------------------------------------
        self.rbtnM = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnM.setGeometry(QtCore.QRect(460, 310, 82, 17))
        self.rbtnM.setObjectName("rbtnM")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 310, 71, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        # Select Position ----------------------------------------------------------
        self.cboxPos = QtWidgets.QComboBox(self.centralwidget)
        self.cboxPos.setGeometry(QtCore.QRect(460, 330, 161, 21))
        self.cboxPos.setObjectName("cboxPos")
        self.cboxPos.InsertPolicy(3)
        self.cboxPos.addItem("Choose position")
        mycursor.execute("select distinct position from employee")
        for x in mycursor:
            item=x[0]
            item=item[0].upper()+item[1:]
            self.cboxPos.addItem(item)

        # Select Order By ----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 360, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("ID")
        self.comboBox.addItem("First Name")
        self.comboBox.addItem("Last name")
        self.comboBox.addItem("Wage")

        # Check Box Asc/Desc ----------------------------------------------------------
        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(580, 360, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")

        # Text Edit Restaurants ----------------------------------------------------------
        self.textRest = QtWidgets.QTextEdit(self.centralwidget)
        self.textRest.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textRest.setObjectName("textRest")
        
        # Labels ----------------------------------------------------------
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 141, 16))
        self.label_4.setObjectName("label_4")

        # Button Search Restaurants ----------------------------------------------------------
        self.butRestS = QtWidgets.QPushButton(self.centralwidget)
        self.butRestS.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.butRestS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butRestS.setText("")
        self.butRestS.setObjectName("butRestS")
        self.butRestS.clicked.connect(self.btnRest)

        # Main Table ----------------------------------------------------------
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
        
        # List View Restaurants ----------------------------------------------------------
        self.listViewRest = QtWidgets.QListWidget(self.centralwidget)
        self.listViewRest.setGeometry(QtCore.QRect(460, 70, 161, 31))
        self.listViewRest.setObjectName("listViewRest")
        self.listViewRest.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Text Edit Reservations ----------------------------------------------------------
        self.testReserv = QtWidgets.QTextEdit(self.centralwidget)
        self.testReserv.setGeometry(QtCore.QRect(460, 130, 111, 31))
        self.testReserv.setObjectName("testReserv")

        # Button Search Reservations ----------------------------------------------------------
        self.butResS = QtWidgets.QPushButton(self.centralwidget)
        self.butResS.setGeometry(QtCore.QRect(590, 130, 31, 31))
        self.butResS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butResS.setText("")
        self.butResS.setObjectName("butResS")
        self.butResS.clicked.connect(self.btnReserv)
        

        # List View Reservations ----------------------------------------------------------
        self.listViewReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listViewReserv.setGeometry(QtCore.QRect(460, 170, 161, 31))
        self.listViewReserv.setObjectName("listViewReserv")
        # self.listViewReserv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewReserv.setStyleSheet("QScrollBar:horizontal{ border: none; background-color: rgba(255,255,255,0);width: 10px;margin: 0px 0px 0px 5px;}")

        # Labels ----------------------------------------------------------
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 110, 111, 16))
        self.label_5.setObjectName("label_5")

        # Button Delete----------------------------------------------------------
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 400, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butDelete.clicked.connect(self.btnDeleteClick)
        
        # Button Add ----------------------------------------------------------
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 400, 171, 31))
        self.butAdd.setObjectName("butAdd")

        # Labels ----------------------------------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 230, 41, 27))
        self.label.setObjectName("label")

        # Text Edit Wage From ----------------------------------------------------------
        self.textFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textFrom.setGeometry(QtCore.QRect(520, 230, 101, 31))
        self.textFrom.setObjectName("textFrom")

        # Labels ----------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 270, 31, 21))
        self.label_2.setObjectName("label_2")

        # Text Edit Wage To ----------------------------------------------------------
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
        args={
        'name_sername':'',
        'rest':'',
        'reserv':'',
        'wage1':'0',
        'wage2': '',
        'gender': '',
        'position':'',
        'order_by':''
        }
        while (self.tableView.rowCount() > 0):
            self.tableView.removeRow(0)
        args['name_sername']=self.textSearch.toPlainText().lower()
        # print(args['name_sername'])
        args['rest']=self.textRest.toPlainText()
        # args['reserv']=self.testReserv.toPlainText()
        if(self.chboxDesc.isChecked()):
            args['order_by']=self.comboBox.currentText().lower().replace(' ', '_')+" desc"
        else:
            args['order_by']=self.comboBox.currentText().lower().replace(' ', '_')
        if(self.rbtnM.isChecked()):
            args['gender']="M"
        elif (self.radioButton_2.isChecked()):
            args['gender']="W"
        if(self.cboxPos.currentText()!="Choose position"):
            args['position']=self.cboxPos.currentText().lower()
            
        if(self.textFrom.toPlainText()==""):
            args['wage1']='0'
        else:
            args['wage1']=self.textFrom.toPlainText()
        if(self.textTo.toPlainText()==""):
            args['wage2']=str(getresult(mycursor.execute("select max(wage) from employee"))[0][0])
        else:
            args['wage2']=self.textTo.toPlainText()
        print(args)
        result=search_all(args)
        
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

    def btnRest(self):
        self.listViewRest.clear()
        if(self.textRest.toPlainText()!=""):
            mycursor.execute("select r.capacity, zc.city, zc.state from zip zc join restaurant r on r.zip=zc.id where r.id="+self.textRest.toPlainText())
            result=getresult(mycursor)[0]
            print(result)
            self.listViewRest.addItem("Capacity: "+str(result[0])+", "+result[1]+", "+result[2])
            mycursor.execute("select reserv.id, reserv.date_start, reserv.date_end, reserv.visitors from reservation reserv join restaurant r on reserv.rest_id=r.id where r.id="+self.textRest.toPlainText())
            result=getresult(mycursor)
            self.listViewReserv.clear()
            self.testReserv.clear()
            for res in result:
                self.listViewReserv.addItem(str(res[0])+": "+str(res[1])+"-"+str(res[2])+", vis: "+str(res[3]))

    def btnReserv(self):
        self.listViewReserv.clear()
        if(self.testReserv.toPlainText()!=""):
            mycursor.execute("select rest.id, reserv.date_start, reserv.date_end, reserv.visitors from restaurant rest join reservation reserv on rest.id=reserv.rest_id where reserv.id="+self.testReserv.toPlainText())
            result=getresult(mycursor)[0]
            print(result)
            self.listViewReserv.addItem(str(result[0]) +": "+str(result[1])+"-"+str(result[2])+", vis: "+str(result[3]))      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

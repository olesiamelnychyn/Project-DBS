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
from GUI import *


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 491)
        SearchWindow.setStyleSheet("background:#fafafe;")
        # SearchWindow.setStyleSheet("background: url(./img/start.png);")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        # Text Edit Search ----------------------------------------------------------
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textSearch.setStyleSheet("")
        self.textSearch.setObjectName("textSearch")
        self.textSearch.setPlaceholderText("Enter name or surname here...")
        self.textSearch.setStyleSheet("background:white;")

        # Button Search ----------------------------------------------------------
        self.butSearch = QtWidgets.QPushButton(self.centralwidget)
        self.butSearch.setGeometry(QtCore.QRect(460, 450, 161, 31))
        self.butSearch.setObjectName("butSearch")
        self.butSearch.clicked.connect(self.btnSeacrhClick)
        self.butSearch.setStyleSheet("background:#f3f3ff;")

        # Labels ----------------------------------------------------------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 210, 121, 16))
        self.label_3.setObjectName("label_3")

        # Radio Buttons Male/Female ----------------------------------------------------------
        self.rbtnM = QtWidgets.QCheckBox(self.centralwidget)
        self.rbtnM.setGeometry(QtCore.QRect(460, 340, 70, 17))
        self.rbtnM.setObjectName("rbtnM")
        self.rbtnF = QtWidgets.QCheckBox(self.centralwidget)
        self.rbtnF.setGeometry(QtCore.QRect(550, 340, 70, 17))
        self.rbtnF.setObjectName("rbtnF")

        # Select Position ----------------------------------------------------------
        self.cboxPos = QtWidgets.QComboBox(self.centralwidget)
        self.cboxPos.setGeometry(QtCore.QRect(460, 360, 161, 21))
        self.cboxPos.setObjectName("cboxPos")
        self.cboxPos.InsertPolicy(3)
        self.cboxPos.setStyleSheet("background:white;")
        self.cboxPos.addItem("Choose position")
        mycursor.execute("select distinct position from employee")
        for x in mycursor:
            item=x[0]
            item=item[0].upper()+item[1:]
            self.cboxPos.addItem(item)

        # Select Order By ----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 390, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("ID")
        self.comboBox.addItem("First Name")
        self.comboBox.addItem("Last name")
        self.comboBox.addItem("Wage")
        self.comboBox.addItem("Restaurant")
        self.comboBox.setStyleSheet("background:white;")

        # Check Box Asc/Desc ----------------------------------------------------------
        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(580, 390, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")
        # self.chboxDesc.setStyleSheet("background:white;")

        # Text Edit Restaurants ----------------------------------------------------------
        self.textRest = QtWidgets.QTextEdit(self.centralwidget)
        self.textRest.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textRest.setObjectName("textRest")
        self.textRest.setStyleSheet("background:white;")
        self.textRest.setPlaceholderText("Restaurant id")
        
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
        # self.butRestS.setStyleSheet("background:white;")

        # Main Table ----------------------------------------------------------
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 421, 391))
        self.tableView.setObjectName("tableView")
        self.tableView.setStyleSheet("background: white;")
        # self.tableView.autoFillBackground()
        self.tableView.setColumnCount(4)
        self.tableView.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.tableView.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("First name"))
        self.tableView.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Last name"))
        self.tableView.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Wage"))
        self.tableView.setColumnWidth(0, 30)
        self.tableView.setColumnWidth(1, 130)
        self.tableView.setColumnWidth(2, 130)
        self.tableView.setColumnWidth(3, 130)
        # self.tableView.setColumnWidth(4, 30)
        self.tableView.verticalHeader().hide()
        # self.tableView.setDisabled(True)
        self.tableView.setStyleSheet("color: black")
        
        # List View Restaurants ----------------------------------------------------------
        self.listViewRest = QtWidgets.QListWidget(self.centralwidget)
        self.listViewRest.setGeometry(QtCore.QRect(460, 70, 161, 41))
        self.listViewRest.setObjectName("listViewRest")
        self.listViewRest.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewRest.setStyleSheet("background:white;")

        # Text Edit Reservations ----------------------------------------------------------
        self.textReserv = QtWidgets.QTextEdit(self.centralwidget)
        self.textReserv.setGeometry(QtCore.QRect(460, 140, 111, 31))
        self.textReserv.setObjectName("textReserv")
        self.textReserv.setStyleSheet("background:white;")
        self.textReserv.setPlaceholderText("Reservation id")

        # Button Search Reservations ----------------------------------------------------------
        self.butResS = QtWidgets.QPushButton(self.centralwidget)
        self.butResS.setGeometry(QtCore.QRect(590, 140, 31, 31))
        self.butResS.setStyleSheet("background-image: url(./img/selbtn.jpg);")
        self.butResS.setText("")
        self.butResS.setObjectName("butResS")
        self.butResS.clicked.connect(self.btnReserv)
        # self.butResS.setStyleSheet("background:white;")
        

        # List View Reservations ----------------------------------------------------------
        self.listViewReserv = QtWidgets.QListWidget(self.centralwidget)
        self.listViewReserv.setGeometry(QtCore.QRect(460, 180, 161, 61))
        self.listViewReserv.setObjectName("listViewReserv")
        # self.listViewReserv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.listViewReserv.setStyleSheet("QScrollBar:horizontal{ border: none; background-color: rgba(255,255,255,0);width: 10px;margin: 0px 0px 0px 5px;}")
        self.listViewReserv.setStyleSheet("background:white;")

        # Labels ----------------------------------------------------------
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 120, 111, 16))
        self.label_5.setObjectName("label_5")

        # Button Delete----------------------------------------------------------
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 450, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butDelete.clicked.connect(self.btnDeleteClick)
        self.butDelete.setStyleSheet("background:#f9dbca;")
        
        # Button Add ----------------------------------------------------------
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 450, 171, 31))
        self.butAdd.setObjectName("butAdd")
        self.butAdd.setStyleSheet("background:#d4f9ca;")

        # Labels ----------------------------------------------------------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 260, 41, 27))
        self.label.setObjectName("label")

        # Text Edit Wage From ----------------------------------------------------------
        self.textFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textFrom.setGeometry(QtCore.QRect(520, 260, 101, 31))
        self.textFrom.setObjectName("textFrom")
        self.textFrom.setStyleSheet("background:white;")

        # Labels ----------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 300, 31, 21))
        self.label_2.setObjectName("label_2")

        # Text Edit Wage To ----------------------------------------------------------
        self.textTo = QtWidgets.QTextEdit(self.centralwidget)
        self.textTo.setGeometry(QtCore.QRect(520, 300, 101, 31))
        self.textTo.setObjectName("textTo")
        self.textTo.setStyleSheet("background:white;")

        # SELECT GROUP BY ----------------------------------------------------------
        self.cboxGroup = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGroup.setGeometry(QtCore.QRect(460, 420, 161, 22))
        self.cboxGroup.setObjectName("cboxGroup")
        self.cboxGroup.setStyleSheet("background:white;")
        self.cboxGroup.addItem("Choose group by")
        self.cboxGroup.addItem("Restaurant")
        self.cboxGroup.addItem("Reservation")
        self.cboxGroup.addItem("Position")
        self.cboxGroup.addItem("Gender")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)
        self.btnSeacrhClick()

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.butSearch.setText(_translate("SearchWindow", "Search"))
        self.label_3.setText(_translate("SearchWindow", "Choose wage range"))
        self.rbtnM.setText(_translate("SearchWindow", "Male"))
        self.rbtnF.setText(_translate("SearchWindow", "Female"))
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
        'order_by':'',
        'group_by':''
        }
        while (self.tableView.rowCount() > 0):
            self.tableView.removeRow(0)
        args['name_sername']=self.textSearch.toPlainText().lower()
        # print(args['name_sername'])
        args['rest']=self.textRest.toPlainText()
        # args['reserv']=self.textReserv.toPlainText()
        if(self.chboxDesc.isChecked()):
            args['order_by']=self.comboBox.currentText().lower().replace(' ', '_')+" desc"
        else:
            args['order_by']=self.comboBox.currentText().lower().replace(' ', '_')
        if(self.rbtnM.isChecked() and not self.rbtnF.isChecked() ):
            args['gender']="M"
        elif (self.rbtnF.isChecked() and not self.rbtnM.isChecked()):
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
        if(self.cboxGroup.currentText()!="Choose group by"):
            args['group_by']=self.cboxGroup.currentText().lower()
        
        
        if(args['group_by']!=''):
            # self.tableView.setColumnCount(2)
            self.tableView.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Summ(Wage)"))
            self.tableView.setColumnWidth(0, 330)
            self.tableView.setColumnWidth(1, 100)
            self.butAdd.setDisabled(True)
            self.butDelete.setDisabled(True)
            self.tableView.setDisabled(True)
            self.tableView.setStyleSheet("color: black")
        elif("restaurant"==args['order_by'] or "restaurant desc"==args['order_by']):
            args['order_by']="rest_id"+args['order_by'][10:]
            print(args['order_by'])
            self.butAdd.setDisabled(False)
            self.butDelete.setDisabled(False)
            self.tableView.setDisabled(False)
            self.tableView.setColumnCount(5)
            self.tableView.setColumnWidth(0, 30)
            self.tableView.setColumnWidth(1, 120)
            self.tableView.setColumnWidth(2, 120)
            self.tableView.setColumnWidth(3, 70)
            self.tableView.setColumnWidth(4, 80)
            self.tableView.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
            self.tableView.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("First name"))
            self.tableView.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Last name"))
            self.tableView.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Wage"))
            self.tableView.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Restaurant ID"))
        else:
            self.butAdd.setDisabled(False)
            self.butDelete.setDisabled(False)
            self.tableView.setDisabled(False)
            self.tableView.setColumnCount(4)
            self.tableView.setColumnWidth(0, 30)
            self.tableView.setColumnWidth(1, 130)
            self.tableView.setColumnWidth(2, 130)
            self.tableView.setColumnWidth(3, 130)
            self.tableView.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
            self.tableView.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("First name"))
            self.tableView.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Last name"))
            self.tableView.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Wage"))

        print(args)
        result=search_all(args)
        for res in result:
            rowPosition = self.tableView.rowCount()
            self.tableView.insertRow(rowPosition)
            if(args['group_by']=="restaurant"):
                mycursor.execute("select r.capacity, zc.city, zc.state from zip zc join restaurant r on r.zip=zc.id where r.id="+str(res[0])+";")
                result2=getresult(mycursor)[0]
                print(result2)
                it="Capacity: "+str(result2[0])+", "+result2[1]+", "+result2[2]
                self.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(it))
            elif(args['group_by']=="reservation"):
                mycursor.execute("select rest.id, reserv.date_start, reserv.date_end, reserv.visitors from restaurant rest join reservation reserv on rest.id=reserv.rest_id where reserv.id="+str(res[0])+";")
                result2=getresult(mycursor)[0]
                print(result2)
                it="Restaurant: "+str(result2[0]) +": "+str(result2[1])+"-"+str(result2[2])+", vis: "+str(result2[3])   
                self.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(it))
            elif(args['group_by']=="gender"):
                if(res[0]=='M'):
                    self.tableView.setItem(rowPosition ,0, QtWidgets.QTableWidgetItem("Male"))
                else:
                    self.tableView.setItem(rowPosition ,0, QtWidgets.QTableWidgetItem("Female"))
            else:
                self.tableView.setItem(rowPosition ,0, QtWidgets.QTableWidgetItem(str(res[0])))
            self.tableView.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(str(res[1])))
            if(args['group_by']==''):
                self.tableView.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
                self.tableView.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))
            if("rest_id"==args['order_by'] or "rest_id desc"==args['order_by']):
                self.tableView.setItem(rowPosition ,4, QtWidgets.QTableWidgetItem(str(res[4])))
        color = QColor(220, 220, 220)
        color2 = QColor(254, 253, 253)
        for j in range(self.tableView.columnCount()):
            for row in range(self.tableView.rowCount()):
                if(row % 2 == 0 ):
                    self.tableView.item(row, j).setBackground(color)
                else:
                    self.tableView.item(row, j).setBackground(color2)
                


    def btnDeleteClick(self):
        if(len(self.tableView.selectionModel().selection().indexes())!=0):
            row=self.tableView.selectionModel().selection().indexes()[0].row()
            item_id=self.tableView.item(row, 0).text()
            delete_employee("employee", item_id)
            while (self.tableView.rowCount() > 0):
                self.tableView.removeRow(0)
            self.btnSeacrhClick()
        # result = search_all()
        # for res in result:
        #     rowPosition = self.tableView.rowCount()
        #     self.tableView.insertRow(rowPosition)
        #     self.tableView.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(res[0])))
        #     self.tableView.setItem(rowPosition ,1, QtWidgets.QTableWidgetItem(res[1]))
        #     self.tableView.setItem(rowPosition ,2, QtWidgets.QTableWidgetItem(res[2]))
        #     self.tableView.setItem(rowPosition ,3, QtWidgets.QTableWidgetItem(str(res[3])))

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
            self.textReserv.clear()
            for res in result:
                self.listViewReserv.addItem(str(res[0])+": "+str(res[1])+"-"+str(res[2])+", vis: "+str(res[3]))

    def btnReserv(self):
        self.listViewReserv.clear()
        if(self.textReserv.toPlainText()!=""):
            mycursor.execute("select rest.id, reserv.date_start, reserv.date_end, reserv.visitors from restaurant rest join reservation reserv on rest.id=reserv.rest_id where reserv.id="+self.textReserv.toPlainText())
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchProdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchProd(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(640, 491)
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
        self.label_3.setGeometry(QtCore.QRect(460, 120, 121, 16))
        self.label_3.setObjectName("label_3")
        self.textSupp = QtWidgets.QTextEdit(self.centralwidget)
        self.textSupp.setGeometry(QtCore.QRect(460, 30, 111, 31))
        self.textSupp.setObjectName("textSupp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 141, 16))
        self.label_4.setObjectName("label_4")
        self.butSuppS = QtWidgets.QPushButton(self.centralwidget)
        self.butSuppS.setGeometry(QtCore.QRect(590, 30, 31, 31))
        self.butSuppS.setStyleSheet("background-image: url(selbtn.jpg);")
        self.butSuppS.setText("")
        self.butSuppS.setObjectName("butSuppS")
        self.listViewSupp = QtWidgets.QListView(self.centralwidget)
        self.listViewSupp.setGeometry(QtCore.QRect(460, 70, 161, 41))
        self.listViewSupp.setObjectName("listViewSupp")
        self.butDelete = QtWidgets.QPushButton(self.centralwidget)
        self.butDelete.setGeometry(QtCore.QRect(260, 450, 171, 31))
        self.butDelete.setObjectName("butDelete")
        self.butAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butAdd.setGeometry(QtCore.QRect(10, 450, 171, 31))
        self.butAdd.setObjectName("butAdd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 140, 41, 27))
        self.label.setObjectName("label")
        self.textFrom = QtWidgets.QTextEdit(self.centralwidget)
        self.textFrom.setGeometry(QtCore.QRect(510, 140, 101, 31))
        self.textFrom.setObjectName("textFrom")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 180, 31, 21))
        self.label_2.setObjectName("label_2")
        self.textTo = QtWidgets.QTextEdit(self.centralwidget)
        self.textTo.setGeometry(QtCore.QRect(510, 180, 101, 31))
        self.textTo.setObjectName("textTo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 421, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 230, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.chboxDesc = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxDesc.setGeometry(QtCore.QRect(570, 230, 70, 17))
        self.chboxDesc.setObjectName("chboxDesc")
        self.cboxGroup = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGroup.setGeometry(QtCore.QRect(460, 270, 161, 22))
        self.cboxGroup.setObjectName("cboxGroup")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchProd()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())

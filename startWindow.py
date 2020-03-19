# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 390)
        MainWindow.setStyleSheet("background-image: url(./img/start.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.butRest = QtWidgets.QPushButton(self.centralwidget)
        self.butRest.setGeometry(QtCore.QRect(40, 40, 131, 131))
        self.butRest.setObjectName("butRest")
        self.butRese = QtWidgets.QPushButton(self.centralwidget)
        self.butRese.setGeometry(QtCore.QRect(410, 40, 131, 131))
        self.butRese.setObjectName("butRese")
        self.butEmp = QtWidgets.QPushButton(self.centralwidget)
        self.butEmp.setGeometry(QtCore.QRect(220, 40, 131, 131))
        self.butEmp.setObjectName("butEmp")
        self.butMeal = QtWidgets.QPushButton(self.centralwidget)
        self.butMeal.setGeometry(QtCore.QRect(40, 220, 131, 131))
        self.butMeal.setObjectName("butMeal")
        self.butProd = QtWidgets.QPushButton(self.centralwidget)
        self.butProd.setGeometry(QtCore.QRect(220, 220, 131, 131))
        self.butProd.setObjectName("butProd")
        self.butSupp = QtWidgets.QPushButton(self.centralwidget)
        self.butSupp.setGeometry(QtCore.QRect(410, 220, 131, 131))
        self.butSupp.setStyleSheet(" font-size: 12px;\n"
"  font-weight: 500;\n"
"color:white;\n"
"background-image: url(btn.png);\n"
"border-radius:5px;")
        self.butSupp.setObjectName("butSupp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.butRest.setText(_translate("MainWindow", "Restaurants"))
        self.butRese.setText(_translate("MainWindow", "Reservations"))
        self.butEmp.setText(_translate("MainWindow", "Employees"))
        self.butMeal.setText(_translate("MainWindow", "Meals"))
        self.butProd.setText(_translate("MainWindow", "Products"))
        self.butSupp.setText(_translate("MainWindow", "Suppliers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

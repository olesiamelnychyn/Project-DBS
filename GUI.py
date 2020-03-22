import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from startWindow import *
from searchEmpWindow import *
from empWindow import *
from PyQt5.QtWidgets import QTableWidgetItem

class MainWin(QtWidgets.QMainWindow):
    

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.butEmp.clicked.connect(self.clicked_btn_employee)
        
    def clicked_btn_employee(self):
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.ui.tableView.itemDoubleClicked.connect(self.clicked_item)
        self.ui.butAdd.clicked.connect(self.btnAddClicked)

    def clicked_item(self):
        print("grt")
        row=self.ui.tableView.selectionModel().selection().indexes()[0].row()
        item_id=self.ui.tableView.item(row, 0).text()
        print("ID "+item_id)
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self, id_emp=item_id)
        self.ui.butDel.clicked.connect(self.Delete_emp)

    def Delete_emp(self):
        delete_employee("employee", self.ui.id_emp)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

    def btnAddClicked(self):
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self)


class EmpWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self,)
        row=self.parent.tableView.selectionModel().selection().indexes()[0].row()
        
        # self.ui.textEmail.insertPlainText(parent.tableView.)


# class SearchEmpWin(QtWidgets.QMainWindow):

#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
        
#         self.ui = Ui_SearchWindow()
#         self.ui.setupUi(self)
#         self.ui.tableView.itemDoubleClicked.connect(self.clicked_item)

#         "here"
#         # clicked.connect(self.clicked_item)

#     def clicked_item(self):
#         print("grt")
#         self.ui = Ui_EmployeeWindow()
#         self.ui.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    print("here")
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
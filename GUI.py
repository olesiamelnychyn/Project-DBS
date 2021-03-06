import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from startWindow import *
from searchWindows import *
from searchWindows.searchEmpWindow import *
from searchWindows.searchSuppWindow import *
from searchWindows.searchEmpWindow import *
from searchWindows.searchMealWindow import *
from searchWindows.searchProdWindow import *
from detailsWindows.mealWindow import *
from detailsWindows.prodWindow import *
from SQLfiles.main import *
# from PyQt5.QtWidgets import QTableWidgetItem

class MainWin(QtWidgets.QMainWindow):
    

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.open_main()
    
    def open_main(self):    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.butEmp.clicked.connect(self.clicked_btn_employee)
        self.ui.butSupp.clicked.connect(self.clicked_supplier)
        self.ui.butMeal.clicked.connect(self.clicked_meal)
        self.ui.butProd.clicked.connect(self.clicked_product)

    # Search product
    def clicked_product(self):
        self.ui = Ui_SearchProd()
        self.ui.setupUi(self)
        self.ui.butAdd.clicked.connect(self.clicked_add_product)
        self.ui.tableWidget.itemDoubleClicked.connect(self.clicked_open_product)
        self.ui.butHome.clicked.connect(self.open_main)

    # one Product
    def clicked_add_product(self):
        self.ui = Ui_ProductWindow()
        self.ui.setupUi(self)
        self.ui.butDel.clicked.connect(self.del_product)
        self.ui.butSave.clicked.connect(self.save_product)

    def del_product(self):
        if(self.ui.id != 0):
            delete_product(self.ui.id)
        self.clicked_product()

    def clicked_open_product(self):
        row=self.ui.tableWidget.selectionModel().selection().indexes()[0].row()
        item_id=self.ui.tableWidget.item(row, 0).text()
        self.ui = Ui_ProductWindow()
        print(item_id)
        self.ui.setupUi(self, id_prod=item_id)
        self.ui.butDel.clicked.connect(self.del_product)
        self.ui.butSave.clicked.connect(self.save_product)

    def save_product(self):
        self.ui.save_clicked()
        self.clicked_product()

    # Search Meal
    def clicked_meal(self):
        self.ui = Ui_SearchMeal()
        self.ui.setupUi(self)
        self.ui.butAdd.clicked.connect(self.clicked_add_meal)
        self.ui.tableWidget.itemDoubleClicked.connect(self.clicked_det_meal)
        self.ui.butHome.clicked.connect(self.open_main)

    # one Meal
    def clicked_add_meal(self):
        self.ui = UiMealWindow()
        self.ui.setupUi(self)
        self.ui.butDel.clicked.connect(self.del_meal)
        self.ui.butSave.clicked.connect(self.save_meal)

    def clicked_det_meal(self):
        row=self.ui.tableWidget.selectionModel().selection().indexes()[0].row()
        item_id=self.ui.tableWidget.item(row, 0).text()
        self.ui = UiMealWindow()
        print(item_id)
        self.ui.setupUi(self, id_meal=item_id)
        self.ui.butDel.clicked.connect(self.del_meal)
        self.ui.butSave.clicked.connect(self.save_meal)

    def save_meal(self):
        self.ui.changes()
        self.clicked_meal()
    
    def del_meal(self):
        if(self.ui.id != 0):
            delete_meals(self.ui.id)
        self.clicked_meal()

    # Search supplier
    def clicked_supplier(self):
        self.ui = Ui_SuppWindow()
        self.ui.setupUi(self)
        self.ui.butHome.clicked.connect(self.open_main)
    
    # Seach employee
    def clicked_btn_employee(self):
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.ui.tableView.itemDoubleClicked.connect(self.clicked_item)
        self.ui.butAdd.clicked.connect(self.btnAddClicked)
        self.ui.butHome.clicked.connect(self.open_main)
        
    # one Employee
    def clicked_item(self):
        print("grt")
        row=self.ui.tableView.selectionModel().selection().indexes()[0].row()
        item_id=self.ui.tableView.item(row, 0).text()
        print("ID "+item_id)
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self, id_emp=item_id)
        self.ui.butDel.clicked.connect(self.Delete_emp)
        self.ui.butSave.clicked.connect(self.Save_employee)

    def Save_employee(self):
        print("here I am")
        self.ui.Save_employee()
        self.clicked_btn_employee()

    def Delete_emp(self):
        if(self.ui.id_emp != 0):
            delete_employee("employee", self.ui.id_emp)
        self.clicked_btn_employee()
        # self.ui = Ui_SearchWindow()
        # self.ui.setupUi(self)

    def btnAddClicked(self):
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self)
        self.ui.butDel.clicked.connect(self.Delete_emp)
        self.ui.butSave.clicked.connect(self.Save_employee)


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
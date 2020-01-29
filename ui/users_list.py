from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from admin import get_customers
from cloud_management import delete_user

users_list = {'First name':'name','Last name':'f_name','Email':'email',
            'National Number':'national_num','id':'id','Password':'password'}#todo we have password column too
class UsersListUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(UsersListUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('users_list.ui', self)  # Load the .ui file
        self.user_id = user_id
        
        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.back.clicked.connect(self.backButtonPressed)


        self.deleteUser = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.deleteUser.clicked.connect(self.deleteButtonPressed)

        self.userlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.userlist.setColumnHidden(5, True)  # column 4 is id

        self.set_table()
    def set_table(self):
        users = get_customers()
        self.userlist.setRowCount(len(users))
        count = 0
        for user in users:
            for key, value in user.items():
                headercount = self.userlist.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.userlist.horizontalHeaderItem(x).text()
                    if m == users_list[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1



    # todo if press back button back to admin_dashboard.ui
    def backButtonPressed(self):
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press delete button then delete row and update table
    def deleteButtonPressed(self):
        row = self.userlist.currentItem().row()
        delete_user(int(self.userlist.item(row,4).text()))
        self.set_table()

    def get_value(object):
        if isinstance(object,QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object,QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QLabel):
            value = object.text()
        if isinstance(object,QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value


def insert_in_rows():
    pass


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = UsersListUi(1)  # Create an instance of our class
    window.show()
    app.exec_()  # Start the application


if __name__ == "__main__":
    main()
# todo maryam passwordo pak kon
#todo maryam oon save edito bardar aberooriziye admin chra bayad usero edit kone
#ye dict doros kon userlist in column haye tableo be column haye data base add kon
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ShowSSHUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(ShowSSHUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('show_ssh.ui', self) # Load the .ui file
        self.user_id = user_id
        self.back = self.findChild(QtWidgets.QPushButton,'bt_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.delete = self.findChild(QtWidgets.QPushButton,'delete_2')
        self.delete.clicked.connect(self.deleteButtonPressed)

        self.ssh_list = self.findChild(QtWidgets.QTableWidget,'tableWidget')
        self.ssh_list.setColumnHidden(5 ,True) #column 5 is id

    #todo if press delete button then delete ssh and update table
    def deleteButtonPressed(self):
        pass

    #todo if press back button back to dashboard
    def backButtonPressed(self):
        #if id=admin ->show all SSHs
        #from admin_dashboard import AdminDashboardUi
        #self.OtherWindow = AdminDashboardUi()
        #self.OtherWindow.show()
        #self.close()
        
        #if id=customer -> show just SSHs of customer
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()
  
    #todo if press one row go to edit_ssh.ui page
    def rowButtonPressed(self):
        pass

    def get_value(object):
        if isinstance(object, QtGui.QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object, QtGui.QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtGui.QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtGui.QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtGui.QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtGui.QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ShowSSHUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
#todo maryam oon id ro hide kon actiono bardar
#todo maryam safeyehaye  manage ro pak kon kolan
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class AdminSnapshotListUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdminSnapshotListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('snapshot_list_admin.ui', self) # Load the .ui file

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.revert = self.findChild(QtWidgets.QPushButton,'revert')
        self.revert.clicked.connect(self.revertButtonPressed)

        self.delete = self.findChild(QtWidgets.QPushButton,'delete_2')
        self.delete.clicked.connect(self.deleteButtonPressed)

        self.snapshot_table = self.findChild(QtWidgets.QPushButton,'tableWidget')
    
    #todo if press revert I don't know 
    def revertButtonPressed(self):
        pass

    #todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        from admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi()
        self.OtherWindow.show()
        self.close()
   
   
    #todo if press delete button then delete ssh and update table
    def deleteButtonPressed(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = AdminSnapshotListUi() # Create an instance of our class
    window.show()
    app.exec_() # Start the application

if __name__ == "__main__":
    main()
#todo pak shavad
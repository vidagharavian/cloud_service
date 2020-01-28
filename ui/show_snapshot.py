from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ShowSnapshotUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(ShowSnapshotUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('show_image.ui', self) # Load the .ui file

        self.createImage = self.findChild(QtWidgets.QPushButton,'create')
        self.createImage.clicked.connect(self.createButtonPressed)

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

    #todo if press back button back to dashboard.ui and pass ids to it
    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()
   
    #todo if press createImage go to CreateSnapshotUi pass user and cloud id
    def createButtonPressed(self):
        from ui.create_snapshot import CreateSnapshotUi
        self.OtherWindow = CreateSnapshotUi()
        self.OtherWindow.show()
        self.close()
   
    #todo if press delete button then delete ssh and update table
    def deleteButtonPressed(self):
        pass
def main():
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = ShowSnapshotUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
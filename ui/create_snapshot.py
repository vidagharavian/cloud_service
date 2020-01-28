from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys
class CreateSnapshotUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(CreateSnapshotUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('create_image.ui', self) # Load the .ui file
        self.user_id = user_id

        self.select_cloud = self.findChild(QtWidgets.QComboBox,'select_cloud')
        self.image_name = self.findChild(QtWidgets.QTextEdit,'image_name')
        
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.take_snapshot = self.findChild(QtWidgets.QPushButton,'take')
        self.take_snapshot.clicked.connect(self.takeButtonPressed)

    #todo if press back button back to dashboard.ui and pass ids
    def backButtonPressed(self):
        #pass ids
        from dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()
    #todo if press back button back to dashboard.ui and update snapshot list
    def takeButtonPressed(self):
        #pass ids
        from dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = CreateSnapshotUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
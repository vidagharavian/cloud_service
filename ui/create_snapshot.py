from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('create_image.ui', self) # Load the .ui file

        self.select_cloud = self.findChild(QtWidgets.QComboBox,'select_cloud')
        self.select_cloud = self.findChild(QtWidgets.QTextEdit,'image_name')
        
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.take_snapshot = self.findChild(QtWidgets.QPushButton,'take')

        self.show()
app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
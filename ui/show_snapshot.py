from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('show_image.ui', self) # Load the .ui file

        self.createImage = self.findChild(QtWidgets.QPushButton,'create')
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.snapshot_table = self.findChild(QtWidgets.QPushButton,'tableWidget')

        self.show()
app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
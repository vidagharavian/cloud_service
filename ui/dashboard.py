from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('dashboard.ui', self) # Load the .ui file

        self.clouds = self.findChild(QtWidgets.QPushButton,'bt_cloud')
        self.keys = self.findChild(QtWidgets.QPushButton,'bt_keys')
        self.snapshot = self.findChild(QtWidgets.QPushButton,'bt_snapshot')
        self.report = self.findChild(QtWidgets.QPushButton,'bt_reports') 
        self.exit = self.findChild(QtWidgets.QPushButton,'bt_exit')

        self.username = self.findChild(QtWidgets.QTextBrowser,'userName')
        self.notif = self.findChild(QtWidgets.QTextBrowser,'notification')
        self.remain = self.findChild(QtWidgets.QTextBrowser,'tb_masraf')
        self.consume = self.findChild(QtWidgets.QTextBrowser,'tb_remainConsume')

        self.show()
app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_public_private_key


class MakeSSHUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(MakeSSHUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ssh_make.ui', self) # Load the .ui file
        self.user_id = user_id
        self.ssh_name = self.findChild(QtWidgets.QTextEdit,'ssh_name')
        self.public_key = self.findChild(QtWidgets.QTextBrowser,'public_key')
        self.private_key = self.findChild(QtWidgets.QTextBrowser,'private_key')
        self.cloud_list = self.findChild(QtWidgets.QComboBox,'cloud_list')
        keys=get_public_private_key()
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.submit = self.findChild(QtWidgets.QPushButton,'submit')
        self.submit.clicked.connect(self.submitButtonPressed)

    #todo when come to this page make one and put it in public_key field (run this after come to ssh_make.py)
    def showPublicKey(self):
        pass
    #todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()
    #todo if press submit button go to dashboard and save public_key and name for the cloud
    def submitButtonPressed(self):
        #first save this ssh for cloud then go to dashboard
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

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
    window = MakeSSHUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
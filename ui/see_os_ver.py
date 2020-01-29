from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys


class SeeOSVersionUI(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None,os_id:int=None):
        super(SeeOSVersionUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('see_os_version.ui', self) # Load the .ui file
        self.user_id = user_id
        self.os_id = os_id

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.add_ver = self.findChild(QtWidgets.QPushButton,'add')
        self.add_ver.clicked.connect(self.addButtonPressed)

        self.os_ver = self.findChild(QtWidgets.QTabWidget,'os_ver_table')

    #todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.os_list import OSList
        self.OtherWindow = OSList(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    #todo if press submit button go to dashboard and save public_key and name for the cloud
    def addButtonPressed(self):
        #first add this os then go to dashboard
        from ui.set_os_version import SetOSVersionUI
        self.OtherWindow = SetOSVersionUI(user_id = self.user_id,os_id=self.os_id)
        self.OtherWindow.show()
        self.close()

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

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = SeeOSVersionUI() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
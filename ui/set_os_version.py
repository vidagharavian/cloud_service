from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys


class SetOSVersionUI(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None,os_id:int=None):
        super(SetOSVersionUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('set_os_version.ui', self) # Load the .ui file
        self.user_id = user_id
        self.os_id = os_id

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.add = self.findChild(QtWidgets.QPushButton,'set')
        self.add.clicked.connect(self.setButtonPressed)

        self.os_ver = self.findChild(QtWidgets.QTextEdit,'ver')

    #todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.see_os_ver import SeeOSVersionUI
        self.OtherWindow = SeeOSVersionUI(user_id = self.user_id,os_id=self.os_id)
        self.OtherWindow.show()
        self.close()
    #todo if press submit button go to dashboard and save public_key and name for the cloud
    def setButtonPressed(self):
        #first add this os then go to dashboard
        from ui.see_os_ver import SeeOSVersionUI
        self.OtherWindow = SeeOSVersionUI(user_id = self.user_id,os_id=self.os_id)
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
    window = SetOSVersionUI() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
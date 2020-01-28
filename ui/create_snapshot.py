from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import take_snapshot, get_user_clouds


class CreateSnapshotUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(CreateSnapshotUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('create_image.ui', self)  # Load the .ui file
        self.user_id = user_id

        self.select_cloud = self.findChild(QtWidgets.QComboBox, 'select_cloud')
        self.image_name = self.findChild(QtWidgets.QTextEdit, 'image_name')
        self.set_cloud()

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.take_snapshot = self.findChild(QtWidgets.QPushButton, 'take')
        self.take_snapshot.clicked.connect(self.takeButtonPressed)

    def set_cloud(self):
        for cloud in get_user_clouds(user_id=self.user_id):
            self.select_cloud.addItem(cloud['host_name'], [str(cloud['id'])])

    # todo if press back button back to dashboard.ui and pass ids
    def backButtonPressed(self):
        # pass ids
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    # todo if press back button back to dashboard.ui and update snapshot list
    def takeButtonPressed(self):
        # pass ids
        take_snapshot(cloud_id=self.select_cloud.itemData(self.select_cloud.currentIndex())[0])
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
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = CreateSnapshotUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()

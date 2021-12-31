from PyQt5 import QtWidgets, uic

import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_os_version, get_versions

version_list = {'Vesion': 'number', 'Version_id': 'os_version_id'}


class SeeOSVersionUI(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, os_id: int = None, is_manager=False):
        super(SeeOSVersionUI, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('see_os_ver.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.os_id = os_id
        self.is_manager = is_manager
        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.add_ver = self.findChild(QtWidgets.QPushButton, 'add')
        self.add_ver.clicked.connect(self.addButtonPressed)

        self.os_ver = self.findChild(QtWidgets.QTabWidget, 'os_ver_table')
        if is_manager:
            self.add_ver.setVisible(False)
        self.create_table()

    # todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.os_list import OSList
        self.OtherWindow = OSList(user_id=self.user_id, is_manager=self.is_manager)
        self.OtherWindow.show()
        self.close()

    # todo if press submit button go to dashboard and save public_key and name for the cloud
    def addButtonPressed(self):
        # first add this os then go to dashboard

        from ui.set_os_version import SetOSVersionUI
        self.OtherWindow = SetOSVersionUI(user_id=self.user_id, os_id=self.os_id)
        self.OtherWindow.show()
        self.close()

    def create_table(self):
        clouds = get_versions(self.os_id)
        self.os_ver_table.setRowCount(len(clouds))
        count = 0
        for cloud in clouds:
            for key, value in cloud.items():
                headercount = self.os_ver_table.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.os_ver_table.horizontalHeaderItem(x).text()
                    if m == version_list[headertext]:
                        self.os_ver_table.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1

    def get_value(object):
        if isinstance(object, QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance(object, QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtWidgets.QSpinBox):
            value = object.value()
        if isinstance(object, QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = SeeOSVersionUI(os_id=1, is_manager=True)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()

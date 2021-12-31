from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_oses

oslist = {'OS Name': 'name', 'Base RAM': 'base_RAM', 'Base CPU': 'base_CPU', 'Base CORE': 'base_CORE',
          'Base DISK': 'base_disk', 'Base Cost': 'base_cost', 'Base Bandwidth': 'base_band_width', 'os_id': 'id'}


class OSList(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, is_manager=False):
        super(OSList, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('os_list.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.is_manager = is_manager
        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.new_os = self.findChild(QtWidgets.QPushButton, 'new_os')
        self.new_os.clicked.connect(self.newOSButtonPressed)

        self.edit_os = self.findChild(QtWidgets.QPushButton, 'edit_os')
        self.edit_os.clicked.connect(self.editOSButtonPressed)

        self.see_ver = self.findChild(QtWidgets.QPushButton, 'see_ver')
        self.see_ver.clicked.connect(self.seeVersionButtonPressed)
        self.os_list = self.findChild(QtWidgets.QTableWidget, 'tableWidget')

        self.os_list.setColumnHidden(7, True)  # id
        if is_manager:
            self.edit_os.setVisible(False)
            self.new_os.setVisible(False)
        self.create_table()

    def create_table(self):
        clouds = get_oses()
        self.os_list.setRowCount(len(clouds))
        count = 0
        for cloud in clouds:
            for key, value in cloud.items():
                headercount = self.os_list.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.os_list.horizontalHeaderItem(x).text()
                    if m == oslist[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1

    def seeVersionButtonPressed(self):
        from ui.see_os_ver import SeeOSVersionUI
        row = self.os_list.currentItem().row()
        self.OtherWindow = SeeOSVersionUI(user_id=self.user_id,os_id=int(self.os_list.item(row,7).text()),is_manager=self.is_manager)  # todo get os_id from table
        self.OtherWindow.show()
        self.close()

    # todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id=self.user_id, is_manager=self.is_manager)
        self.OtherWindow.show()
        self.close()

    # todo if press submit button go to dashboard and save public_key and name for the cloud
    def newOSButtonPressed(self):
        # first add this os then go to dashboard
        from ui.os_create import CreateOS
        self.OtherWindow = CreateOS(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    def editOSButtonPressed(self):
        # todo update os
        pass

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
    window = OSList()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()

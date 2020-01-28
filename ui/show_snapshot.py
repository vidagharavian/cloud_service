from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

snapshot_list = {'cloud_id': 'cloud', 'Date creation': 'date_created', 'minimum CPU': 'cpu_amount',
                 ' minimum RAM': 'ram_amount', 'minimum disk': 'disk_amount', 'minimum core': 'core_amount',
                 'Bound width': 'band_width'}
from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_snapshots


class ShowSnapshotUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(ShowSnapshotUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('show_image.ui', self)  # Load the .ui file
        self.user_id = user_id

        self.createImage = self.findChild(QtWidgets.QPushButton, 'create')
        self.createImage.clicked.connect(self.createButtonPressed)

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.revert = self.findChild(QtWidgets.QPushButton, 'revert')
        self.revert.clicked.connect(self.revertButtonPressed)

        self.delete = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.delete.clicked.connect(self.deleteButtonPressed)

        self.snapshot_table = self.findChild(QtWidgets.QPushButton, 'tableWidget')
        self.create_table()

    # todo if press revert I don't know
    def revertButtonPressed(self):
        pass

    # todo if press back button back to dashboard.ui and pass ids to it
    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    # todo if press createImage go to CreateSnapshotUi pass user and cloud id
    def createButtonPressed(self):
        from ui.create_snapshot import CreateSnapshotUi
        self.OtherWindow = CreateSnapshotUi()
        self.OtherWindow.show()
        self.close()

    # todo if press delete button then delete ssh and update table
    def deleteButtonPressed(self):
        pass

    def create_table(self):
        snapshots = get_snapshots(user_id=self.user_id)
        self.snapshot_table.setRowCount(len(snapshots))
        count = 0
        for cloud in snapshots:
            for key, value in cloud.items():
                headercount = self.cloudlist.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.cloudlist.horizontalHeaderItem(x).text()
                    if m == snapshot_list[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
        count += 1


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = ShowSnapshotUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()

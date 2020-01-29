from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_public_private_key, get_user_clouds, get_ssh, get_cloud, create_ssh


# todo maryam ssh_id age dasht edite
class MakeSSHUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, ssh_id: int = None):
        super(MakeSSHUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('ssh_make.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.ssh_id = ssh_id
        self.ssh_name = self.findChild(QtWidgets.QTextEdit, 'ssh_name')
        self.public_key = self.findChild(QtWidgets.QTextBrowser, 'public_key')
        self.private_key = self.findChild(QtWidgets.QTextBrowser, 'private_key')
        self.cloud_list = self.findChild(QtWidgets.QComboBox, 'cloud_list')
        self.private_label = self.findChild(QtWidgets.QLabel, 'label_3')
        self.label = self.findChild(QtWidgets.QLabel, 'label_4')

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit')
        self.submit.clicked.connect(self.submitButtonPressed)
        self.edit = self.findChild(QtWidgets.QPushButton, 'edit') 
        self.edit.clicked.connect(self.editButtonPressed)

        if ssh_id is not None:
            self.private_key.setVisible(False)
            self.private_label.setVisible(False)
            self.label.setVisible(False)
            self.edit.setVisible(False)
            self.submit.setVisible(True)

        else:
            self.private_key.setVisible(True)
            self.private_label.setVisible(True)
            self.label.setVisible(True)
            self.edit.setVisible(True)
            self.submit.setVisible(False)

        self.set_defaults()

    def set_clouds(self, is_update):
        if not is_update:
            self.cloud_list.addItem('--')
            default_cloud_id = 0
        else:
            ssh = get_ssh(self.ssh_id)[0]
            cloud = get_cloud(ssh['cloud_id'])[0]
            self.cloud_list.addItem(cloud['host_name'], [str(cloud['id'])])
            default_cloud_id = cloud['id']
        for cloud in get_user_clouds(user_id=self.user_id):
            if cloud['id'] != default_cloud_id:
                self.cloud_list.addItem(cloud['host_name'], [str(cloud['id'])])

    def set_defaults(self):
        if self.ssh_id is None:
            keys = get_public_private_key()
            self.public_key.setText(keys['public_key'])
            self.private_key.setText(keys['private_key'])
            self.set_clouds(False)
        else:
            ssh = get_ssh(self.ssh_id)[0]
            self.public_key.setText(ssh['key'])
            self.ssh_name.setText(ssh['name'])
            self.set_clouds(True)

    # todo when come to this page make one and put it in public_key field (run this after come to ssh_make.py)

    # todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.show_ssh import ShowSSHUi
        self.OtherWindow = ShowSSHUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press submit button go to dashboard and save public_key and name for the cloud
    def submitButtonPressed(self):
        # first save this ssh for cloud then go to dashboard
        try:
            create_ssh(self.get_value(self.ssh_name), self.user_id, self.get_value(self.public_key),
                       self.cloud_list.itemData(self.cloud_list.currentIndex())[0])
        except Exception:
            create_ssh(self.get_value(self.ssh_name), self.user_id, self.get_value(self.public_key),
                       self.cloud_list.itemData(self.cloud_list.currentIndex())[0])
        from ui.show_ssh import ShowSSHUi
        self.OtherWindow = ShowSSHUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    def editButtonPressed(self):
        #todo edit ssh
        from ui.show_ssh import ShowSSHUi
        self.OtherWindow = ShowSSHUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()


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
    window = MakeSSHUi(19)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()

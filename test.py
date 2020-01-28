from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=2048
)
private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption())
public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)
print(str(public_key)+'\n')
print(str(private_key))
print('maryam')

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

self.cpu = QtGui.QtWidgets.QSpinBox()
self.cpu.setValue(11)
get_value(cpu)


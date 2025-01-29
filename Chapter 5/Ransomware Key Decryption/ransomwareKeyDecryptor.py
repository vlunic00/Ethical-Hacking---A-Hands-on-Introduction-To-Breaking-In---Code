from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import socketserver
import base64

class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):
        encrypted_key_file = self.request.recv(1024).strip()

        with open(encrypted_key_file, "rb") as encrypted_file:
            encrypted_key = encrypted_file.read()

        #INSERT YOUR PRIVATE KEY FILE HERE
        private_key_file = ""

        with open(private_key_file, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                backend=default_backend(),
                password = None
            )

        original_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
)
)

self.request.sendall(original_key)

if __name__ == "__main__":
	HOST, PORT = "", 8000
	
	tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)
	try:
		tcpServer.serve_forever()
	except Exception as e:
		print("There was an error: ", e)

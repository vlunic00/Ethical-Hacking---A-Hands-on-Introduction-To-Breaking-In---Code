from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import socketserver
import base64
import socket
import ssl
import threading

client_cert = 'INSERT CLIENT CERTIFICATE PATH HERE'
server_key = 'INSERT SERVER KEY PATH HERE'
server_cert = 'INSERT SERVER CERTIFICATE PATH HERE'

port = 8080
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile = client_cert)
context.load_cert_chain(certfile = server_cert, keyfile = server_key)
context.options |= ssl.OP_SINGLE_ECDH_USE
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

def handler(conn):
	encrypted_key = conn.recv(4096)
	
	with open("INSERT PRIVATE KEY PATH HERE", "rb") as key_file:
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
	
	conn.send(original_key)
	conn.close()
	
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(("", port))
	sock.listen(5)
	with context.wrap_socket(sock, server_side = True) as ssock:
		while True:
			conn, addr = ssock.accept()
			print(addr)
			handlerThread = threading.Thread(target = handler, args = (conn,))
			handlerThread.start() 

# Ransomware Client Server Connection<br><br>
The challenge here was to create a ransomware client, which can encrypt a certian file with a symmetric key, and then encrypt the symmetric key with his public key (as described in the first task).
However, the client should then also be able to decrypt the file, witht the help of the server.<br>
The server's function is to decrypt the symmetric key using the attacker's private key.<br><br>
The client can both encrypt and decrypt the file. The decryption happens by contacting the server and receiving the decrypted symmetric key.<br><br>
To run the script, the cryptography library is needed.<br>
You can install it with pip (among other options) using `pip install cryptography`<br><br>
The client takes 2 arguments; mode [encrypt/decrypt] and the path to the file you want to encrypt/decrypt (if the file is in the same directory, only its name is needed).<br>
To run the client, use `python ransomwareClient.py <mode> <file_path>`<br>
To start the server, run its code in a terminal using `python ransomwareKeyDecryptor.py`<br>


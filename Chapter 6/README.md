# Encrypted Ransomware Client/Server<br><br>
We took the code for the ransomware client and server from Chapter 5 and made their communication secure with TLS.<br>
To establish TLS, first we needed to generate keyes and certificates for both the client and the server.<br>
We achieved this using openssl, with the following commands:<br>
`openssl req -new -newkey rsa:3072 -days 365 -nodes -x509-keyout server.key -out server.crt` - server private key & certificate<br>
`openssl req -new -newkey rsa:3072 -days 365 -nodes -x509-keyout client.key -out client.crt` - client private key & certificate<br>
After you've generated the required keyes and certificates, put their file paths in the places marked in the code.<br><br>
To run the script, the cryptography library is needed.<br>
You can install it with pip (among other options) using `pip install cryptography`<br><br>
The client takes 2 arguments; mode [encrypt/decrypt] and the path to the file you want to encrypt/decrypt (if the file is in the same directory, only its name is needed).<br>
To run the client, use `python ransomwareClient.py <mode> <file_path>`<br>
To start the server, run its code in a different terminal using `python ransomwareKeyDecryptor.py`

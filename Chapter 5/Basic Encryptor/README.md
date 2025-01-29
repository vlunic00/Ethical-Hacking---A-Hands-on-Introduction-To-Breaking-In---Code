# Ransomware-like file encryptor<br><br>
A file encryption script that works similar to how ransomware does, in that it uses a symmetric key which is itself encrypted by the hackers public key.
The public key is generated with openssl:
1. We generate a public-private key pair with `openssl genrsa -out pub_priv_pair.key 1024`
2. Extract the public key with `openssl rsa -in pub_priv_pair.key -pubout -out public_key.key`
<br><br>

In the code, link to your specific key and file at the marked places<br><br>
The current file in plaintext said: "IF YOU CAN READ THIS, IT ISN'T ENCRYPTED"<br><br>
The encrypted file reads: "gAAAAABnmoMYoFvWV6TjeaFmDToKb-Mo5uZHZ6YC11hMsnuJrIyLJBNJ5JFika-03z7xXgkBZ0cge_Zi4bJO8ZNIABfFSZ0ef8xNqvKmiC6QnzJ2LmnahM9ZYMadP1mf9jpcfid11OjM"<br><br>
To run the script, the cryptography library is needed.<br>
You can install it with (for example) pip, using `pip install cryptography`

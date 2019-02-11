import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import data as Data_Module
import ast

def generate_keys():
    # A function to generate random keys for users 
    modulus_length = 1024
    key = RSA.generate(modulus_length)
    pub_key = key.publickey()
    return key, pub_key

def encrypt_private_key(a_message, private_key):
    # Encrypt anything
    encryptor = PKCS1_OAEP.new(private_key)
    decrypted_msg = encryptor.encrypt(a_message)
    print(decrypted_msg)
    return decrypted_msg

def encrypt():
    # Get data from the data module and encrypt the data
    keys = generate_keys()
    key = keys[0]
    pub_key = keys[1]
    f = open ('encryption.txt', 'w')
    f.write(key) #write ciphertext to file
    f.close()
    data = Data_Module.data_pull()
    encrypt_private_key(data,key)


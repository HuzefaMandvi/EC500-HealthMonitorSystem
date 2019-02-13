from cryptography.fernet import Fernet

def decrypt():
    with open('private.key', 'rb') as f:
        key = f.readline()
    fernet = Fernet(key)
    with open('private.dat') as f:
        data = bytearray(f.read(), 'utf-8')
    encrypted = fernet.decrypt(bytes(data))
    with open('decrypted.dat','wb') as f:
        f.write(encrypted)

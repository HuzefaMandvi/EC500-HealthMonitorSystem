from cryptography.fernet import Fernet

def decrypt(keyFile, filename):
    # fernet = Fernet(key)
    # with open('private.dat') as f:
    #     data = bytes(f.read(), 'utf-8')
    # decrypted = fernet.decrypt(data)
    # with open('decrypted.dat','wb') as f:
    #     f.write(decrypted)
    # return decrypted
    with open(keyFile, 'rb') as f:
        key = f.readline()
    fernet = Fernet(key)
    with open(filename,'r') as f:
        lines = f.readlines()
    print(lines[1])
    for line in lines:
        decrypted = fernet.decrypt(line.encode())
        f= open(filename + "_decrypted", 'a') 
        f.write(decrypted.decode('utf-8') +  "\n")
        f.close()

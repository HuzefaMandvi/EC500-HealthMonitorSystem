import time
from encryption import encrypt
from decryption import decrypt
def insertData(P_ID, data):
    filename = str(P_ID) + "_data"
    keyFile = str(P_ID) + ".key"
    with open(keyFile, 'r') as f:
        key = f.readline()
    f = open(filename, "a")
    ts = time.time()
    data = str(P_ID) + "\tTIME: " + str(ts) + "\t" +str(data ) 
    encrypted = encrypt(data,key)
    f.write(encrypted.decode('utf-8')+ "\n")

def getData(P_ID):
    filename = str(P_ID) + "_data"
    keyFile = str(P_ID) + ".key"
    decrypt(keyFile,filename)
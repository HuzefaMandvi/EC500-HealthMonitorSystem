import time
def insertData(P_ID, data):
    f = open("database.txt", "a")
    ts = time.time();
    f.write(str(P_ID) + "\tTIME: " + str(ts) + "\t" +str(data) + "\n")

def getData(P_ID):
    with open('database.txt','r') as f:
            line = f.readline()
            while line:
                line = f.readline()
                if(line[:8]==str(P_ID)):
                    print(line)

    


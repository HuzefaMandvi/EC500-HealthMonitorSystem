import random
import threading
import time

hr = 0
bp1 = 0
bp2 = 0
bo = 0

def init():
        hr = random.randint(60, 100)
        bp1 = random.randint(120, 140)
        bp2 = random.randint(80, 90)
        bo = random.randint(75, 100)
        t = threading.Thread(target=callback)
        t.start()

def callback():
        hr = random.randint(60, 100)
        bp1 = random.randint(120, 140)
        bp2 = random.randint(80, 90)
        bo = random.randint(75, 100)
        time.sleep(random.randint(1,10))
        callback()

def data_pull():

        pdata = {
                "heart_rate": hr,
                "blood_pressure1": bp1,
                "blood_pressure2": bp2,
                "blood_oxygen": bo,
        }
        return pdata

import random

def data_pull():
        hr = random.randint(60, 100)
        bp1 = random.randint(120, 140)
        bp2 = random.randint(80, 90)
        bo = random.randint(75, 100)

        pdata = {
                "heart_rate": hr,
                "blood_pressure1": bp1,
                "blood_pressure2": bp2,
                "blood_oxygen": bo,
        }
        return pdata

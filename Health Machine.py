import random
#a heart rate, b bpm1, c bpm2, d bo


a = random.randint(60, 100)
b = random.randint(120, 140)
c = random.randint(80, 90)
d = random.randint(75, 100)

pdata = {
        "heart_rate": a,
        "blood_pressure1": b,
        "blood_pressure2": c,
        "blood_oxygen": d
}
print pdata.get("heart_rate")
print pdata.get("blood_pressure1")
print pdata.get("blood_pressure2")
print pdata.get("blood_oxygen")

import datetime


def page_doctor(data, identifier, is_anomalous):
    if is_anomalous:
        measure_thing = ""
        value = [0]
        if identifier == 0x01:
            measure_thing = "heart rate"
            value = data.get("heart_rate")
        if identifier == 0x02:
            measure_thing = "blood pressure"
            value[0] = data.get("blood_pressure1")
            value.append(data.get("blood_pressure2"))
        if identifier == 0x03:
            measure_thing = "blood oxygen level"
            value[0] = data.get("blood_oxygen")

        print("Uh oh Doctor, the patient's", measure_thing, "is", value, "at", datetime.datetime.now())
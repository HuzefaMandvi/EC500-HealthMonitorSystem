import datetime


def page_doctor(value, identifier, is_anomalous):
    if is_anomalous:
        measure_thing = ""
        if identifier == 0x01:
            measure_thing = "heart rate"
        if identifier == 0x02:
            measure_thing = "blood pressure"
        if identifier == 0x03:
            measure_thing = "blood oxygen level"

        print("Uh oh Doctor, the patient's", measure_thing, "is", value, "at", datetime.datetime.now())
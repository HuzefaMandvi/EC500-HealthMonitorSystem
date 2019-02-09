
def Error_Handler(data):
    hr_reading = data.get("heart_rate")
    bp1_reading = data.get(“blood_pressure1”)
    bp2_reading = data.get(“blood_pressure2”)
    bo_reading = data.get(“blood_oxygen”)

    alert = false

    if bp1_reading > 140 or bp1_reading < 120 or bp2_reading > 90 or bp2_reading < 80:
        alert = true

    if hr_reading > 120 or hr_reading < 50:
        alert = true

    if bo_reading > 110 or bo_reading < 70:
        alert = true

    return alert
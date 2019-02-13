
def Error_Handler(data):
    hr_reading = data.get("heart_rate")
    bp1_reading = data.get("blood_pressure1")
    bp2_reading = data.get("blood_pressure2")
    bo_reading = data.get("blood_oxygen")

    alert = False

    if bp1_reading > 140 or bp1_reading < 120 or bp2_reading > 90 or bp2_reading < 80:
        alert = True

    if hr_reading > 120 or hr_reading < 50:
        alert = True

    if bo_reading > 110 or bo_reading < 70:
        alert = True

    return alert

def check_hr(data):
    hr_reading = data.get("heart_rate")
    if hr_reading > 120 or hr_reading < 50:
        return True

def check_bp(data):
    bp = data.get("blood_pressure1")
    if bp> 140 or bp< 120:
        return True

def check_bo(data):
    bo_reading = data.get("blood_oxygen")
    if bo_reading > 110 or bo_reading < 70:
        return True

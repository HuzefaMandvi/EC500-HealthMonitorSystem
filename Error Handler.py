
def Error_Handler(bp1_reading, bp2_reading, bo_reading, hr_reading):
    alert = false

    if bp1_reading > 140 or bp1_reading < 120 or bp2_reading > 90 or bp2_reading < 80:
        alert = true

    if hr_reading > 120 or hr_reading < 50:
        alert = true

    if bo_reading > 110 or bo_reading < 70:
        alert = true

    return alert
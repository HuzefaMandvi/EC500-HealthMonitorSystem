class Error_Handler:
    def __init__(self, bp1_reading, bp2_reading, bo_reading, hr_reading):
        self.bp1_reading = pdata.get("blood_pressure1")
        self.bp2_reading = pdata.get("blood_pressure2")
        self.hr_reading = pdata.get("blood_oxygen")
        self.bo_reading = pdata.get("heart_rate")

    def bad_bp(self):
       if self.bp1_reading > 140 or self.bp1_reading < 120 or self.bp2_reading > 90 or self.bp2_reading < 80:
           alert = true
       else alert = false


    def bad_hr(self):
        if self.hr_reading > 120 or self.hr_reading < 50:
            alert = true
        else alert = false

    def bad_bo(self):
        if self.hr_reading > 110 or self.hr_reading < 70:
            alert = true
        else alert = false 
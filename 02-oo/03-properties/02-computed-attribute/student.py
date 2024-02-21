# Write your code here
class BMICalculator:
    
    def __init__(self, weight_in_kg, height_in_m):
        self.weigth_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def bmi(self):
        return self.weigth_in_kg / self.height_in_m**2
    
    @property
    def category(self):
        if self.bmi < 18.5:
            return f"underweight"
        elif self.bmi < 25:
            return f"normal"
        else:
            return f"overweight"
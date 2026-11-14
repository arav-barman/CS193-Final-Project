class UserProfile:  # stores a user's personal information for calorie calculations
    def __init__(self, age, height_ft, height_in, sex, weight_lb, activity_level):
        self.sex = sex
        self.age = age
        self.weight_lb = weight_lb #in lbs
        self.height_ft = height_ft
        self.height_in = height_in
        self.activity_level = activity_level

    def get_height_cm(self):
        total_inches = self.height_ft * 12 + self.height_in
        total_cm = total_inches * 2.54
        return total_cm

    def get_kg_weight(self):
        return self.weight_lb * 0.45359237

    def calculate_bmr(self): #BMR: the number of calories you burn in a day at rest without the input of exercise 
        bmr = (10 * self.get_kg_weight()) + (6.25 * self.get_height_cm()) - (5 * self.age)
        if self.sex.lower() == "male":
            return bmr + 5
        else:
            return bmr - 161


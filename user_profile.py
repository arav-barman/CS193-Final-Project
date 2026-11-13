class UserProfile:  # stores a user's personal information for calorie calculations
    def __init__(self, age, height_ft, height_in, gender, weight, activity_level):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height_ft = height_ft
        self.height_in = height_in
        self.activity_level = activity_level

    def get_height_cm(self):
        total_inches = self.height_ft * 12 + self.height_in
        total_cm = total_inches * 2.54
        return total_cm
class UserProfile:  
    # stores a user's personal information for calorie calculations and easier to implement a saved history by storing data in a json file
    def __init__(self, age, height_ft, height_in, sex, weight_lb, activity_level):
        self.sex = sex
        self.age = age
        self.weight_lb = weight_lb 
        #height is broken up into two compoents feet and inches rather than a decimal because it is unatural for a human to know their decimal value in only feet
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
        #Mifflin-St Jeor is used over the older Harris-Benedict equation because it is generally more accurate when calculating an individual's resting calories 
        #this formula is defined metric units, so some conversions had to be done in order to be in the correct form 
        bmr = (10 * self.get_kg_weight()) + (6.25 * self.get_height_cm()) - (5 * self.age)
        if self.sex.lower() == "male":
            return bmr + 5
        else:
            return bmr - 161
        
    def calculate_tdee(self): #estimated total calories burned in a day, including respective activity level
        #a dictionary lookup rather a long chain of if/elif statements that directly identifies a fixed multiplier based on the user input
        #caught a type here once: 155 insteaed of 1.55 tahat gave a TDEE value of approximatey 277000 but so changed it, and thoroughly tested that every level works 
        activity_multiplier = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
        return self.calculate_bmr() * activity_multiplier[self.activity_level]

    def recommend_goal(self, plan):  #recommended daily calories based on the user's plan
        #plan is a parameter rather an attribute because the user has a chioce to choose their plan of action
        #-500 per day is roughly 1lb lost per week; +250 is a small bulk and adds mostly muscle rather than fat
        recommendations = {"lose": -500, "maintain": 0, "bulk": 250}
        goal = self.calculate_tdee() + recommendations[plan]
        #Never recommend less than the BMR because it would too aggressive to lose that weight, especially for someone who is lighter
        return max(self.calculate_bmr(), goal)

class DailyLog: #stores one day's calorie data within the DailyLog class 
    def __init__(self): #created the constructor with three initial attributes 
        self.calories_eaten = 0 #tracks the calories eaten by the user
        self.calories_burned = 0 #tracks the calories burned by the user
        self.goal = 0 #tracks the daily goal inputted by the user 

    def add_eaten(self, eaten: float):
        self.calories_eaten += eaten

    def add_burned(self, burned: float):
        self.calories_burned += burned

    def set_goal(self, goal: float):
        self.goal = goal 

    def get_net_calories(self):
        net_calories = self.calories_eaten - self.calories_burned
        return net_calories
    
    def goal_check(self):
        return self.goal - self.get_net_calories()

    def reset(self):
        self.calories_eaten = 0 
        self.calories_burned = 0
        self.goal = 0
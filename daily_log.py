class DailyLog: 
    #this class only stores and calculates; it never prints or asks for an input
    #to add a GUI, keeping the interactiveness part of the prgogram in main.py means a future Tkinter GUI can reuse this class unchanged
    def __init__(self): 
        self.calories_eaten = 0 
        self.calories_burned = 0 
        self.goal = 0  #0 means no goal set; main.py checks for this before comparing 

    def add_eaten(self, eaten: float):
        self.calories_eaten += eaten

    def add_burned(self, burned: float):
        self.calories_burned += burned

    def set_goal(self, goal: float):
        #originally had += but changed it to = because a goal stays constant and doesn't accumulate; only changes if the user wants a different goal 
        self.goal = goal 

    def get_net_calories(self):
        net_calories = self.calories_eaten - self.calories_burned
        return net_calories
    
    def goal_check(self):
        #returns a signed number instead of message
        #positive means under the goal, while negative means over the goal
        return self.goal - self.get_net_calories()

    def reset(self):
        self.calories_eaten = 0 
        self.calories_burned = 0
        self.goal = 0
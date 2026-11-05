class DailyLog: #created the DailyLog class 
    def __init__(self): #created the constructor with three initial attributes 
        self.calories_eaten = 0 #tracks the calories eaten by the user
        self.calories_burned = 0 #tracks the calories burned by the user
        self.goal = 0 #tracks the daily goal inputted by theh user 

    def add_eaten(self, eaten):
        self.calories_eaten += eaten

    def add_burned(self, burned):
        self.calories_burned += burned
        
    

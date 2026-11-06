from daily_log import DailyLog

log = DailyLog()
eaten_input = float(input("Enter the number of calories you ate: "))
burned_input = float(input("Enter the number of calories you ate: "))
goal_input = float(input("Enter your caloric goal: "))
log.add_eaten(eaten_input)
log.add_burned(burned_input)
log.add_goal(goal_input)
print(log.calories_eaten)
print(log.calories_burned)
print(log.goal)
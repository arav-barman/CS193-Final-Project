from daily_log import DailyLog

log = DailyLog()
eaten_input = float(input("Enter the number of calories you ate: "))
burned_input = float(input("Enter the number of calories you burned: "))
goal_input = float(input("Enter your caloric goal: "))
log.add_eaten(eaten_input)
log.add_burned(burned_input)
log.add_goal(goal_input)
net_calories = log.get_net_calories()
difference = log.goal_check()

if difference >= 0:
    print(f"You have met your goal! You are {int(difference)} calories under")
else:
     print(f"You did not meet your goal. You are {int(-1*difference)} calories over")
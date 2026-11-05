from daily_log import DailyLog

log = DailyLog()
user_input = float(input("Enter the number of calories you ate: "))
log.add_eaten(user_input)
print(log.calories_eaten)
from daily_log import DailyLog
from user_profile import UserProfile

log = DailyLog()

def get_number(prompt):
     continue_loop = True
     while continue_loop:
          try:
               value = float(input(prompt))
          except ValueError:
               print("Please input a number.\n")
               continue  
          if value < 0:
               print("Please enter a number 0 or greater.\n")
               continue
          return value 

user_continues = True 
while user_continues:
     print("\n1. Log calories eaten")
     print("2. Log calories burned")
     print("3. Set daily goal")
     print("4. Check goal")
     print("5. Summary")
     print("6. Reset")
     print("7. Quit\n")

     choice = input("Choose an option: ")
     if choice == "1":
           eaten_input = get_number("Enter the number of calories you ate: ") 
           log.add_eaten(eaten_input)
     elif choice == "2":
          burned_input = get_number("Enter the number of calories you burned: ")
          log.add_burned(burned_input)
     elif choice == "3":
          goal_input = get_number("Enter your caloric goal: ")
          log.set_goal(goal_input)
     elif choice == "4":
          if log.goal == 0:
               print("You have not set a goal yet.")
          else:
               net_calories = log.get_net_calories()
               difference = log.goal_check()
               print(f"Net Calories: {net_calories:.0f} ({log.calories_eaten:.0f} eaten - {log.calories_burned:.0f} burned)")
               if difference >= 0:
                    print(f"You have met your goal! You are {difference:.0f} calories under your {log.goal:.0f} calorie goal.")
               else:
                    print(f"You did not meet your goal. You are {-1*difference:.0f} calories over your {log.goal:.0f} calorie goal.") 
     elif choice == "5":
          net_calories = log.get_net_calories()
          difference = log.goal_check()
          print("\n--- Daily Summary ---")
          print(f"Current Calories Eaten:  {log.calories_eaten:.0f}")
          print(f"Current Calories Burned: {log.calories_burned:.0f}")
          print(f"Net Calories:            {net_calories:.0f}")
          if log.goal == 0:
               print("Goal:                    not set yet")
          else:
               print(f"Goal:                    {log.goal:.0f}")
               if difference >= 0:
                    print(f"Status: You are {difference:.0f} calories under your goal")
               else:
                    print(f"Status: You are {-1*difference:.0f} calories over your goal")
     elif choice == "6":
          confirm = input("Are you sure you want to reset all values? (Y/N): ")
          if confirm.lower() == "y":
               log.reset()
               print("All values have been reset.")
          else:
               print("Reset cancelled.")
     elif choice == "7":
          print("Goodbye!")
          user_continues = False
     else:
          print("Invalid option. Please enter a number from 1 to 7.")
          


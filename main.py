from daily_log import DailyLog

log = DailyLog()

user_continues = True 
while user_continues:
     print("\n1. Log calories eaten")
     print("2. Log calories burned")
     print("3. Set daily goal")
     print("4. Check goal")
     print("5. Quit\n")

     choice = input("Choose an option: ")
     if choice == "1":
           eaten_input = float(input("Enter the number of calories you ate: "))
           log.add_eaten(eaten_input)
     elif choice == "2":
          burned_input = float(input("Enter the number of calories you burned: "))
          log.add_burned(burned_input)
     elif choice == "3":
          goal_input = float(input("Enter your caloric goal: "))
          log.set_goal(goal_input)
     elif choice == "4":
          net_calories = log.get_net_calories()
          difference = log.goal_check()
          print(f"Net Calories: {round((net_calories), 2)}")
          if difference >= 0:
               print(f"You have met your goal! You are {int(difference)} calories under.")
          else:
               print(f"You did not meet your goal. You are {int(-1*difference)} calories over.") 
     elif choice == "5":
          print("\nGoodbye!")
          user_continues = False
     else:
          print("Invalid option. Please enter a number from 1 to 5.")
          


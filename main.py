from daily_log import DailyLog
from user_profile import UserProfile

log = DailyLog()

def get_number(prompt):
     #Validating the user input remained here rather than in one of the classes because checking what the user typed is the job of the menu code, not the classes that store and calculate data
     continue_loop = True
     while continue_loop:
          try:
               #the try and except blocks were needed because if the user inputted the wrong data type (ex: float("xyz")), it would crash the program
               value = float(input(prompt))
          except ValueError:
               print("Please input a number\n")
               continue  
          if value < 0:
               print("Please enter a number 0 or greater\n")
               continue
          return value 

user_continues = True 
while user_continues:
     print("\n1. Log calories eaten")
     print("2. Log calories burned")
     print("3. Set daily goal")
     print("4. Check goal")
     print("5. Summary")
     print("6. Calorie Calculator")
     print("7. Reset")
     print("8. Quit\n")

     choice = input("Choose an option: ") #kept a string instead of converting to an integer because strings can't crash, so a bad input simply falls through to the else branch 
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
          if log.goal == 0: #without this check, an unset goal would make every user look over their goal when in reality they do not have one set, and the program would provide misleading information
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
          #Option 4 provides a quick check whether the user was over or under the goal, whereas this option provides an entire breakdown 
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
          #Each user has their profile rebuilt on every run instead of being saved elsewhere
          #Having a saved history feature is in the Eisenhower Matrix, however, it was left out on this branch to focus on the calorie calculator 
          age = get_number("Enter your age in years: ")
          height_ft = get_number("Enter your height (feet): ")
          height_in = get_number("Enter your height (remaining in inches): ")
          while height_in >= 12:
               print("Inches must be less than 12.")
               height_in = get_number("Enter your height (remaining in inches): ")
          weight_lb = get_number("Enter your weight in pounds: ")
          
          sex = input("Enter your sex (male/female): ").strip().lower()
          #Originally had an "or" statement, but every input would satisfy one side so I changed it to "and" because nothing would equal both male and female
          while sex != "male" and sex != "female":
               print("Please enter male or female")
               sex = input("Enter your sex (male/female):  ").strip().lower()

          print("\nActivity level:")
          print("1. Sedentary (little or no exercise)")
          print("2. Lightly active (1-3 days/week)")
          print("3. Moderately active (3-5 days/week)")
          print("4. Very active (6-7 days/week)")
          print("5. Extremely active (physical job + training)")
          activity = int(get_number("Enter your activity level (1-5): ")) #an integer because the multiplier dictionary keys are whole numbers; without this type conversion, a float or any other primitive type would raise a KeyError
          while activity < 1 or activity > 5:
               activity = int(get_number("Enter your activity level (1-5): "))

          profile = UserProfile(age=age, height_ft=height_ft, height_in=height_in, sex=sex, weight_lb= weight_lb, activity_level=activity)
          print(f"\nBMR (Calories Burned at Rest): {profile.calculate_bmr():.0f}")
          print(f"TDEE (Estimated Calories to Maintain Weight): {profile.calculate_tdee():.0f}")

          plan = input("\nWhat is your plan? (lose/maintain/bulk): ").strip().lower()
          while plan != "lose" and plan != "maintain" and plan != "bulk":
               print("Please enter lose, maintain, or bulk")
               plan = input("What is your plan? (lose/maintain/bulk): ").strip().lower()
          recommend = profile.recommend_goal(plan)
          print(f"Recommended Daily Goal: {recommend:.0f} calories")
          print("Note: these are estimates, not medical advice.")

          #the recommendation is offered to be set as the user's goal but not applied automatically; asks the user whether they want this value outputted to be set as their daily goal or not 
          use_goal = input("\nWould you like to use this recommendation as your daily goal? (Y/N): ").strip().lower()
          if use_goal == "y":
               log.set_goal(recommend)
               print(f"Daily Goal: {log.goal:.0f} calories")
          else:
               print("Goal not changed")

     elif choice == "7":
          #Confirmation guard if the user accidentally inputted 7 and wiped the whole day's data
          confirm = input("Are you sure you want to reset all values? (Y/N): ")
          if confirm.lower() == "y":
               log.reset()
               print("All values have been reset.")
          else:
               print("Reset cancelled.")
     elif choice == "8":
          print("Goodbye!")
          user_continues = False
     else:
          print("Invalid option. Please enter a number from 1 to 8.")
          


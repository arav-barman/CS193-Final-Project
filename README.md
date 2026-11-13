# Calorie Tracker

A Python command-line program for tracking daily calories eaten and burned, setting a calorie goal, and checking whether you met it.

## The Problem

Keeping track of calories has been a challenge for me, especially as someone who works out consistently while trying to lose weight and gain muscle. Many apps require a paid subscription or have a cluttered interface, so I wanted to build a simple application that lets people like me track their daily calories, set a goal, and quickly see whether they are on track or going over their limit.

## How It Works

Version 1.0 is a menu-driven command-line program. The user can:

- **Log calories eaten** from meals and snacks, added to a running daily total
- **Log calories burned** from exercise
- **Set a daily calorie goal**, which replaces any previous goal
- **Check the goal:** the program calculates net calories (eaten − burned), compares them to the goal, and reports how far under or over the user is
- **View a daily summary** of calories eaten, calories burned, net calories, the goal, and current status
- **Reset all values** to start a new day, with a confirmation prompt to prevent accidental resets
- **Quit** the program

The menu repeats after every action until the user quits. Invalid input, such as letters, negative numbers, or invalid menu choices, is rejected without crashing the program.

The program is split into two files:

- `daily_log.py` contains the `DailyLog` class, which stores and calculates the day's data.
- `main.py` handles the menu, user input, and output.

![System diagram](docs/system_diagram.png)

The full feature breakdown is in the [Eisenhower Matrix](docs/eisenhower_matrix.pdf).

## Tech Stack

- **Language:** Python 3
- **Libraries:** none (Python standard library only)
- **External tools:** Git, GitHub, VS Code

## Setup

You only need Python 3 installed. Check with:

```bash
python3 --version
```

Then clone the repo:

```bash
git clone https://github.com/arav-barman/CS193-Final-Project.git
cd CS193-Final-Project
```

## Usage

Run the program:

```bash
python3 main.py
```

Example session (the menu is shown once; it reappears before every choice):

```
1. Log calories eaten
2. Log calories burned
3. Set daily goal
4. Check goal
5. Summary
6. Reset
7. Quit

Choose an option: 3
Enter your caloric goal: 2000

Choose an option: 1
Enter the number of calories you ate: 2300

Choose an option: 2
Enter the number of calories you burned: 400

Choose an option: 4
Net Calories: 1900 (2300 eaten - 400 burned)
You have met your goal! You are 100 calories under your 2000 calorie goal.

Choose an option: 5

--- Daily Summary ---
Current Calories Eaten:  2300
Current Calories Burned: 400
Net Calories:            1900
Goal:                    2000
Status: You are 100 calories under your goal

Choose an option: 6
Are you sure you want to reset all values? (Y/N): y
All values have been reset.

Choose an option: 7
Goodbye!
```

## Roadmap

Planned features from the "Schedule" quadrant of my Eisenhower Matrix:

- [ ] Calorie calculator that recommends a daily goal based on age, height, weight, and activity level
- [ ] Saved history so data carries over between sessions
- [ ] Weekly summary of average net calories and days the goal was met
- [ ] Tkinter GUI to replace the command-line interface

## Author

Arav Barman · [GitHub](https://github.com/arav-barman)
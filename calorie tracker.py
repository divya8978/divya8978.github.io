#Name: Divya Marndi
#Date: 09-10-2025
# Project Title: Daily Calorie Tracker CLI

print(" Welcome to the Daily Calorie Tracker CLI! ")
print("Track your meals, calculate calories, and stay healthy!\n")
meal_name = []
meal_calories = []
n_meals = int(input("How many meals do you want to log today?\n "))

for i in range(n_meals):
    meal = input(f"Enter the name of meal #{i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_name.append(meal)
    meal_calories.append(calories)
    total_calories = sum(meal_calories)
avg_calories = total_calories / len(meal_calories)

limit = float(input("\nEnter your daily calorie limit: "))
if total_calories > limit:
    print("\n Warning: You've exceeded your daily limit!")
else:
    print("\n You're within your calorie limit.")
print("\n--- Daily Summary ---")
print("Meal Name\tCalories")
print("-" * 25)
for i in range(len(meal_name)):  

    print(f"{meal_name[i]}\t\t{meal_calories[i]}")

print("-" * 25)
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{avg_calories:.2f}")

import datetime

save = input("\nDo you want to save this session? (yes/no): ").lower()
if save == "yes":
    with open("calorie_log.txt", "w") as file:
        file.write(f"Daily Calorie Tracker Log\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        for i in range(len(meal_name)):
            file.write(f"{meal_name[i]} - {meal_calories[i]} cal\n")
        file.write(f"\nTotal: {total_calories}\nAverage: {avg_calories:.2f}\n")
        if total_calories > limit:
            file.write("Status: Exceeded limit\n")
        else:
            file.write("Status: Within limit\n")
    print("Session saved to calorie_log.txt!")

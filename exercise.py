# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    vowels = ["a", "e", "i", "o", "u"]
    letter = input("Enter a letter: ")

    if letter.isalpha():
        if letter.lower() in vowels:
            print(f"The letter {letter} is a vowel")
        else:
            print(f"The letter {letter} is a consonant")
    else:
        print(f"{letter} is not a letter")

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = input("Enter your age: ")
    if age.isnumeric():
        if int(age) < 0:
            print("Please enter a number above 0")
        elif int(age) >= 18:
            print(f"You're age is {age} and you are eligible to vote")
        else:
            print(f"You're age is {age} and you are not eligible to vote")
    else:
        print(f"Please enter a number")

# Call the function
check_voting_eligibility()



# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input("Enter your dogs age: ")
    if dog_age.isnumeric() and int(dog_age) > 2:
        dog_years = ((int(dog_age) - 2) * 7) + 20
        print(f"Your dog is about {dog_years} in dog years")
    elif dog_age.isnumeric() and int(dog_age) == 2:
        print(f"Your dog is about 20 years old")
    elif dog_age.isnumeric() and int(dog_age) == 1:
        print(f"Your dog is about 10 years old")

# Call the function
calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    raining = input("Is it raining? (yes/no): ")
    cold = input("Is it Cold out? (yes/no): ")
    if (
        cold.isalpha()
        and cold.lower() != "yes"
        or cold.lower() != "no"
        and raining.isalpha()
        and raining.lower() != "yes"
        or raining.lower() != "no"
    ):
        print("Please only enter yes or no")
    if cold.lower() == "yes" and raining.lower() == "yes":
        print("Wear a waterproof jacket")
    elif cold.lower() == "yes" and raining.lower() == "no":
        print("Wear a warm coat")
    elif cold.lower() == "no" and raining.lower() == "yes":
        print("Carry and umbrella")
    elif cold.lower() == "no" and raining.lower() == "no":
        print("Wear light clothing")

# Call the function
weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input("enter a month of the year (e.g. Jan for January): ")
    day = input("enter a day of the month: ")
    if day.isnumeric() and month.isalpha():
        if month.lower() == "jan" or month.lower() == "feb":
            print(f"{month} {day} is in Winter")
        elif (month.lower() == "dec" and int(day) >= 21 and int(day) <= 31) or (
            month.lower() == "mar" and int(day) <= 19 and int(day) >= 1
        ):
            print(f"{month} {day} is in Winter")
        elif month.lower() == "apr" or month.lower() == "may":
            print(f"{month} {day} is in Spring")
        elif (month.lower() == "mar" and int(day) >= 20 and int(day) <= 31) or (
            month.lower() == "jun" and int(day) <= 20 and int(day) >= 1
        ):
            print(f"{month} {day} is in Spring")
        elif month.lower() == "jul" or month.lower() == "aug":
            print(f"{month} {day} is in Summer")
        elif (month.lower() == "jun" and int(day) >= 21 and int(day) <= 30) or (
            month.lower() == "sep" and int(day) <= 21 and int(day) >= 1
        ):
            print(f"{month} {day} is in Summer")
        elif month.lower() == "oct" or month.lower() == "nov":
            print(f"{month} {day} is in Fall")
        elif (month.lower() == "sep" and int(day) >= 22 and int(day) <= 30) or (
            month.lower() == "dec" and int(day) <= 20 and int(day) >= 1
        ):
            print(f"{month} {day} is in Fall")
    else:
        print("Please enter a proper month and day")

# Call the function
determine_season()

#No exercise 6 in lab materials

#Level Up

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.


def guess_number():
    import math
    import random
    random_number = math.floor(random.random() * 100)
    guesses = 5
    correct = False
    while guesses > 0:
        guess = input(
            f"You have {guesses} guesses. Choose a number between 1 and 100: "
        )
        guesses -= 1
        if guess.isnumeric():

            if int(guess) > random_number:
                print(f"Your guess of {guess} was to high")

            elif int(guess) < random_number:
                print(f"Your guess of {guess} was to low")

            elif int(guess) == random_number:

                correct = True
                print(
                    f"Congratulations, you guessed {guess}, and the number was {random_number} and it took you {5 - guesses} guess(es)"
                )
                break

        else:
            print("Please enter a proper number")
        if guesses == 0 and not correct:
            print(f"Sorry the number was {random_number} and you are now out of guesses")

# Call the function
guess_number()


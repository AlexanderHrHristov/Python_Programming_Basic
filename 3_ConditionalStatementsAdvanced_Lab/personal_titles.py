# Read user input
age = float(input())
gender = input()

user_output = ""

# Logic
if gender == "f":
    if age >= 16:
        user_output = "Ms."
    else:
        user_output = "Miss"
elif gender == "m":
    if age >= 16:
        user_output = "Mr."
    else:
        user_output = "Master"

# User output

print(user_output)



# User input
day_time = int(input())
day_of_week = input()

# Working hours - Monday - Saturday 10:00 - 18:00

# Logic
if not day_of_week == "Sunday" and 10 <= day_time <= 18:
    print("open")
else:
    print("closed")


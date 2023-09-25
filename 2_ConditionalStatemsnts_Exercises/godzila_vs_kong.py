movie_budget = float(input())
number_of_statist = int(input())
clothing_price = float(input())

decor_expence = movie_budget * 0.1

if number_of_statist > 150:
    clothing_cost = number_of_statist * clothing_price * 0.9
else:
    clothing_cost = number_of_statist * clothing_price

total_expences = decor_expence + clothing_cost
difference = abs(movie_budget - total_expences)

if movie_budget < total_expences:
    print ("Not enough money!")
    print(f"Wingard needs {differеnce:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {differеnce:.2f} leva left.")

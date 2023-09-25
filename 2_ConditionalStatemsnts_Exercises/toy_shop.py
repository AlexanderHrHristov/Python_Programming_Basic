excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = 2.60
dolls_price = 3.00
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

count_of_toys = puzzles + dolls + bears + minions + trucks

incomes_from_toys = puzzles * puzzles_price\
                    + dolls * dolls_price\
                    + bears * bears_price\
                    + minions * minions_price\
                    + trucks * trucks_price

if count_of_toys >= 50:
    incomes_from_toys = incomes_from_toys * 0.75
total_sum = incomes_from_toys * 0.90

difference = abs(total_sum - excursion_price)

if total_sum - excursion_price >=0 :
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
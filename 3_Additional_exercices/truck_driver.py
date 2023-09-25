season = input()
distance = float(input())

working_months = 4
profit = 0
# taxes = 10%

if distance <= 5000:
    if season == 'Spring' or season == 'Autumn':
        profit = distance * 0.75
    elif season == 'Summer':
        profit = distance * 0.90
    elif season == 'Winter':
        profit = distance * 1.05
elif 5000 < distance <= 10000:
    if season == 'Spring' or season == 'Autumn':
        profit = distance * 0.95
    elif season == 'Summer':
        profit = distance * 1.10
    elif season == 'Winter':
        profit = distance * 1.25
elif 10000 < distance <= 20000:
    profit = distance * 1.45

net_profit = working_months * profit * 0.90

print(f'{net_profit:.2f}')
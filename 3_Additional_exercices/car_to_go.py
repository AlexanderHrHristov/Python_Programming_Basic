budget = float(input())
season = input()

car_class = ''
car_type = ''
needed_money = 0

if 0 < budget <= 100:
    car_class = 'Economy class'
elif 100 < budget <= 500:
    car_class = 'Compact class'
elif budget > 500:
    car_class = 'Luxury class'

if car_class == 'Economy class':
    if season == 'Summer':
        car_type = 'Cabrio'
        budget *= 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        budget *= 0.65

elif car_class == 'Compact class':
    if season == 'Summer':
        car_type = 'Cabrio'
        budget *= 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        budget *= 0.80

elif car_class == 'Luxury class':
    car_type = 'Jeep'
    budget *= 0.90

print(f'{car_class}')
print(f'{car_type} - {budget:.2f}')

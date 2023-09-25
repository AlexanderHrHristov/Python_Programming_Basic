budget = float(input())
season = input()

location = ''
accomodation = ''
price = 0

if 0 < budget <= 1000:
    accomodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45

elif 1000 < budget <= 3000:
    accomodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60

elif budget > 3000:
    accomodation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.90
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.90

print(f'{location} - {accomodation} - {price:.2f}')
num_chrisanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
holiday = input()

chrisanthemums_summer_price = 2.00
roses_summer_price = 4.10
tulips_summer_price = 2.50

chrisanthemums_winter_price = 3.75
roses_winter_price = 4.50
tulips_winter_price = 4.15

arrangement_price = 2.00

total_flowers = num_tulips + num_roses + num_chrisanthemums
bouquet_price = 0



if season == 'Spring' or season == 'Summer':
    bouquet_price = (num_chrisanthemums * chrisanthemums_summer_price) + (num_roses * roses_summer_price) \
                    + (num_tulips * tulips_summer_price)
elif season == 'Autumn' or season == 'Winter':
    bouquet_price = (num_chrisanthemums * chrisanthemums_winter_price) + (num_roses * roses_winter_price) \
                    + (num_tulips * tulips_winter_price)
if holiday == 'Y':
    bouquet_price *= 1.15

if num_tulips > 7 and season == 'Spring':
    bouquet_price *= 0.95

if num_roses >= 10 and season == 'Winter':
    bouquet_price *= 0.90

if total_flowers > 20:
    bouquet_price *= 0.80

bouquet_price += 2.00

print(f'{bouquet_price:.2f}')



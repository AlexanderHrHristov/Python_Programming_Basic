month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights > 7 and nights <= 14:
        studio_price *= nights
        studio_price -= studio_price * 0.05
    elif nights > 14:
        studio_price *= nights
        studio_price -= studio_price * 0.3
    else:   
        studio_price *= nights
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= nights
        studio_price -= studio_price * 0.2
    else:
        studio_price *= nights
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    studio_price *= nights

if nights > 14:
    apartment_price *= nights
    apartment_price -= apartment_price * 0.1
else:
    apartment_price *= nights

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
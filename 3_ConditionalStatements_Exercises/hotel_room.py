# Read user input
month = input()
nights = int(input())

# Logic
studio_amount = 0
apartament_amount = 0

# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.


if month == "May" or month == "October":
    if nights <= 7:
        studio_amount = nights * 50
        apartament_amount = nights * 65
    elif nights > 14:
        studio_amount = nights * 50 * 0.7
        apartament_amount = nights *  65 * 0.9
    else:
        studio_amount = nights * 50 * 0.95
        apartament_amount = nights * 65
elif month == "June" or month == "Septeber":
    if nights > 14:
        studio_amount = nights * 75.2 * 0.8
        apartament_amount = nights * 68.7 * 0.9
    elif nights <= 14:
        studio_amount = nights * 75.2
        apartament_amount = nights * 68.7

elif month == "July" or month == "August":
    if nights > 14:
        studio_amount = nights * 76
        apartament_amount = nights * 77 * 0.9
    else:
        studio_amount = nights * 76
        apartament_amount = nights * 77


# Print output
print(f"Apartment: {apartament_amount:.2f} lv.")
print(f"Studio: {studio_amount:.2f} lv.")

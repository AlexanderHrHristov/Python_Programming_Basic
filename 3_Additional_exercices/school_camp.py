season = input()
groups_type = input()
count_of_students = int(input())
number_of_nights = int(input())

sport = ''
price_per_night = 0

if season == 'Winter':
    if groups_type == 'girls':
        sport = 'Gymnastics'
        total_amount = number_of_nights * count_of_students * 9.60
    elif groups_type == 'boys':
        sport = 'Judo'
        total_amount = number_of_nights * count_of_students * 9.60
    elif groups_type == 'mixed':
        sport = 'Ski'
        total_amount = number_of_nights * count_of_students * 10.00
elif season == 'Spring':
    if groups_type == 'girls':
        sport = 'Athletics'
        total_amount = number_of_nights * count_of_students * 7.20
    elif groups_type == 'boys':
        sport = 'Tennis'
        total_amount = number_of_nights * count_of_students * 7.20
    elif groups_type == 'mixed':
        sport = 'Cycling'
        total_amount = number_of_nights * count_of_students * 9.50
elif season == 'Summer':
    if groups_type == 'girls':
        sport = 'Volleyball'
        total_amount = number_of_nights * count_of_students * 15.00
    elif groups_type == 'boys':
        sport = 'Football'
        total_amount = number_of_nights * count_of_students * 15.00
    elif groups_type == 'mixed':
        sport = 'Swimming'
        total_amount = number_of_nights * count_of_students * 20.00

if count_of_students >= 50:
    total_amount *= 0.5
elif 20 <= count_of_students < 50:
    total_amount *= 0.85
elif 10 <= count_of_students < 20:
    total_amount *= 0.95

print(f'{sport} {total_amount:.2f} lv.')

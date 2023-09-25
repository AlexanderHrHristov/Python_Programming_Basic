total_budget = float(input())
category_ticket = input()
number_of_people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

needed_money = 0

if category_ticket == 'VIP':
    if number_of_people <= 4:
        needed_money = (number_of_people * vip_ticket) + total_budget * 0.75
    elif 5 <= number_of_people <= 9:
        needed_money = (number_of_people * vip_ticket) + total_budget * 0.60
    elif 10 <= number_of_people <= 24:
        needed_money = (number_of_people * vip_ticket) + total_budget * 0.50
    elif 25 <= number_of_people <= 49:
        needed_money = (number_of_people * vip_ticket) + total_budget * 0.40
    elif number_of_people >= 50:
        needed_money = (number_of_people * vip_ticket) + total_budget * 0.25

elif category_ticket == 'Normal':
    if number_of_people <= 4:
        needed_money = (number_of_people * normal_ticket) + total_budget * 0.75
    elif 5 <= number_of_people <= 9:
        needed_money = (number_of_people * normal_ticket) + total_budget * 0.60
    elif 10 <= number_of_people <= 24:
        needed_money = (number_of_people * normal_ticket) + total_budget * 0.50
    elif 25 <= number_of_people <= 49:
        needed_money = (number_of_people * normal_ticket) + total_budget * 0.40
    elif number_of_people >= 50:
        needed_money = (number_of_people * normal_ticket) + total_budget * 0.25

difference = abs(total_budget - needed_money)

if total_budget > needed_money:
    print (f'Yes! You have {difference:.2f} leva left.')
else:
    print (f'Not enough money! You need {difference:.2f} leva.')

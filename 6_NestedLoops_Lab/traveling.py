saved_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    price = float(input())
    saved_money = 0
    while True:
        income = float(input())
        saved_money += income
        if saved_money >= price:
            print(f'Going to {destination}!')
            break

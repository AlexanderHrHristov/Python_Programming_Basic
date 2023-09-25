fuel_type = input()
fuel_quantity = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

needed_money = 0
discount = 0

if fuel_type == 'Gasoline':
    if  club_card == 'No':
        if fuel_quantity < 20:
            needed_money = gasoline_price * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = gasoline_price * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = gasoline_price * fuel_quantity * 0.90
    if club_card == 'Yes':
        if fuel_quantity < 20:
            needed_money = (gasoline_price - 0.18) * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = (gasoline_price - 0.18) * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = (gasoline_price - 0.18) * fuel_quantity * 0.90

if fuel_type == 'Diesel':
    if club_card == 'No':
        if fuel_quantity < 20:
            needed_money = diesel_price * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = diesel_price * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = diesel_price * fuel_quantity * 0.90
    if club_card == 'Yes':
        if fuel_quantity < 20:
            needed_money = (diesel_price - 0.12) * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = (diesel_price - 0.12) * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = (diesel_price - 0.12) * fuel_quantity * 0.90

if fuel_type == 'Gas':
    if  club_card == 'No':
        if fuel_quantity < 20:
            needed_money = gas_price * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = gas_price * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = gas_price * fuel_quantity * 0.90
    if club_card == 'Yes':
        if fuel_quantity < 20:
            needed_money = (gas_price - 0.08) * fuel_quantity
        elif 20 <= fuel_quantity <= 25:
            needed_money = (gas_price - 0.08) * fuel_quantity * 0.92
        elif 25 < fuel_quantity:
            needed_money = (gas_price - 0.08) * fuel_quantity * 0.90


print(f'{needed_money:.2f} lv.')

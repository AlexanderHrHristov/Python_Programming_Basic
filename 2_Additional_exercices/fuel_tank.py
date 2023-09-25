type_of_fuel = input()
fuel_available = float(input())

if type_of_fuel == 'Diesel':
    if fuel_available >= 25:
        print(f'You have enough diesel.')
    elif fuel_available < 25:
        print(f'Fill your tank with diesel!')

elif type_of_fuel == 'Gasoline':
    if fuel_available >= 25:
        print(f'You have enough gasoline.')
    elif fuel_available < 25:
        print(f'Fill your tank with gasoline!')

elif type_of_fuel == 'Gas':
    if fuel_available >= 25:
        print(f'You have enough gas.')
    elif fuel_available < 25:
        print(f'Fill your tank with gas!')

else:
    print(f'Invalid fuel!')


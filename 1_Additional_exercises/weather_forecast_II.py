outside_temperature = float(input())

if 5.00 <= outside_temperature <= 11.90:
    print('Cold')

elif 12.00 <= outside_temperature <= 14.90:
    print('Cool')

elif 15.00 <= outside_temperature <= 20.00:
    print('Mild')

elif 20.10 <= outside_temperature <= 25.90:
    print('Warm')

elif 26.00 <= outside_temperature <= 35.00:
    print('Hot')
else:
    print('unknown')



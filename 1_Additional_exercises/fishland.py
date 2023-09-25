mackerel_price = float(input())
sprat_price = float(input())
bonito_weight = float(input())
safrid_weight = float(input())
mussels_weight = int(input())

bonito_price = mackerel_price * 1.6
safrid_price = sprat_price * 1.8
musseles_price = 7.50

needed_money = bonito_price * bonito_weight + safrid_price * safrid_weight + musseles_price * mussels_weight

print(f'{needed_money:.2f}')


# Цена на паламуда = 6.90 + 6.90 * 0.60 = 11.04 лв. за килограм
# Сума паламуд = 1.5 * 11.04 = 16.56
# Цена на сафрид = 4.20 + 4.20 * 0.80 =  7.56 лв. за килограм
# Сума сафрид = 2.5 * 7.56 = 18.90
# Сума миди = 1 * 7.50 = 7.50
# Сметка = 16.56 + 18.90 + 7.50 = 42.96





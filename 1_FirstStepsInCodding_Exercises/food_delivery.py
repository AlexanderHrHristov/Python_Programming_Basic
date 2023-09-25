count_chiken_menus = int(input())
count_fish_menus = int(input())
count_vege_menus = int(input())

#Цена за пилешките менюта: 2 броя * 10.35 = 20.70
#Цена за менютата с риба: 4 броя * 12.40 = 49.60
#Цена за вегетарианските менюта: 3 броя * 8.15 = 24.45
#Обща цена на менютата: 20.70 + 49.60 + 24.45 = 94.75
#Цена на десерта: 20% от 94.75 = 18.95
#Цена на доставка: 2.50 (по условие)
#Обща цена на поръчката: 94.75 + 18.95 + 2.50 = 116.20

price_chiken_menu = 10.35
price_fish_menu = 12.40
price_vege_menu = 8.15
price_desserts = (price_chiken_menu + price_fish_menu + price_vege_menu)
price_of_delivery = 2.50

amount_chiken_menus = count_chiken_menus * price_chiken_menu
amount_fish_menus = count_fish_menus * price_fish_menu
amount_vege_menus = round(count_vege_menus * price_vege_menu, 2)
amount_menu_food = amount_vege_menus + amount_chiken_menus + amount_fish_menus
amount_desserts = amount_menu_food * 20/100
amount_for_delivery = price_of_delivery

final_result = amount_menu_food + amount_desserts + amount_for_delivery

print(final_result)

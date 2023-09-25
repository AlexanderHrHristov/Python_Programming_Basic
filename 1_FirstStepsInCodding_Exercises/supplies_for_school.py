#Пакет химикали - 5.80 лв.
#Пакет маркери - 7.20 лв.
#Препарат - 1.20 лв (за литър)

#Вход
#От конзолата се четат 4 числа:

#Брой пакети химикали - цяло число в интервала [0...100]
#Брой пакети маркери - цяло число в интервала [0...100]
#Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#Процент намаление - цяло число в интервала [0...100]

#Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.

    count_pen_pack = int(input())
    count_marker_pack = int(input())
    qtity_cleaner = int(input())
    percent_discount = int(input())

    pen_pack_price = 5.80
    markers_pack_price = 7.20
    cleaner_price_per_liter = 1.20

    pens_amount = count_pen_pack * pen_pack_price
    markers_amount = count_marker_pack * markers_pack_price
    detergent_amount = qtity_cleaner * cleaner_price_per_liter

    sum_for_materials = pens_amount + markers_amount + detergent_amount

    total_sum = sum_for_materials - (sum_for_materials * percent_discount /100)

    print(total_sum)

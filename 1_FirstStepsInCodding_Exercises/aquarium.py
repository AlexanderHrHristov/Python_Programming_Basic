#Вход
#Дължина в см – цяло число в интервала [10 … 500]
#Широчина в см – цяло число в интервала [10 … 300]
#Височина в см – цяло число в интервала [10… 200]
#Процент – реално число в интервала [0.000 … 100.000]

length_of_aquarium = int(input())
width_of_aquarium = int(input())
height_of_aquarium = int(input())
percent_other = float(input())

total_volume_litres = (length_of_aquarium * width_of_aquarium * height_of_aquarium)/1000
water_volume_litres = total_volume_litres - (total_volume_litres * percent_other/100)

print(water_volume_litres)

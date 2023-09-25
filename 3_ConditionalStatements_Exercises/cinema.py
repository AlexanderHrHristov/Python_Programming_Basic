# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.
#

type_of_movie = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns
ticket_price = 0

if type_of_movie == "Premiere":
    ticket_price = 12
elif type_of_movie == "Normal":
    ticket_price = 7.5
elif type_of_movie == "Discount":
    ticket_price = 5
total_income = ticket_price * cinema_capacity

print(f"{total_income:.2f}")

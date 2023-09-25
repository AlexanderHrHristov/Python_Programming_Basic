# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	    3.80	2.80	3	    2.50
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

# User input

kind_of_flowers = input()
numbers_of_flowers = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

needed_money = 0


# Logic
if kind_of_flowers == "Roses":
    if numbers_of_flowers > 80:
        needed_money = roses_price * numbers_of_flowers * 0.9
    else:
        needed_money = roses_price * numbers_of_flowers

if kind_of_flowers == "Dahlias":
    if numbers_of_flowers > 90:
        needed_money = dahlias_price * numbers_of_flowers * 0.85
    else:
        needed_money = dahlias_price * numbers_of_flowers

if kind_of_flowers == "Tulips":
    if numbers_of_flowers > 80:
        needed_money = tulips_price * numbers_of_flowers * 0.85
    else:
        needed_money = tulips_price * numbers_of_flowers

if kind_of_flowers == "Narcissus":
    if numbers_of_flowers < 120:
        needed_money = narcissus_price * numbers_of_flowers * 1.15
    else:
        needed_money = narcissus_price * numbers_of_flowers

if kind_of_flowers == "Gladiolus":
    if numbers_of_flowers < 80:
        needed_money = gladiolus_price * numbers_of_flowers * 1.2
    else:
        needed_money = gladiolus_price * numbers_of_flowers

difference = abs(budget - needed_money)
left_money = (budget - needed_money)


if left_money >= 0:
    print(f"Hey, you have a great garden with {numbers_of_flowers} {kind_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
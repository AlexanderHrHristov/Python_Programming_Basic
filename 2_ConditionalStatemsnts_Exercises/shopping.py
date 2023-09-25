budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

video_cards_price = number_of_video_cards * 250
processor_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

needed_money = video_cards_price \
               + number_of_processors * processor_price \
               + number_of_ram * ram_price

if number_of_video_cards > number_of_processors:
    needed_money *= 0.85 # needed_money = needed_money * 0.85
difference = abs(budget - needed_money)

if budget >= needed_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

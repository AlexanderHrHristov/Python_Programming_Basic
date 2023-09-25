num_junior_bikers = int(input())
num_senior_bikers = int(input())
type_of_trace = input()

junior_price_trail = 5.50
junior_price_cross = 8
junior_price_downhill = 12.25
junior_price_road = 20
senior_price_trail = 7
senior_price_cross = 9.50
senior_price_downhill = 13.75
senior_price_road = 21.50

total_bikers = num_junior_bikers + num_senior_bikers
total_money = 0

if type_of_trace == 'trail':
    total_money = num_junior_bikers * junior_price_trail + num_senior_bikers * senior_price_trail
elif type_of_trace == 'downhill':
    total_money = num_junior_bikers * junior_price_downhill + num_senior_bikers * senior_price_downhill
elif type_of_trace == 'road':
    total_money = num_junior_bikers * junior_price_road + num_senior_bikers * senior_price_road
elif type_of_trace == 'cross-country':
     if total_bikers < 50:
         total_money = num_junior_bikers * junior_price_cross + num_senior_bikers * senior_price_cross
     else:
         total_money = (num_junior_bikers * junior_price_cross + num_senior_bikers * senior_price_cross) * 0.75

expenses = total_money * 0.05

donation = total_money - expenses

print(f'{donation:.2f}')
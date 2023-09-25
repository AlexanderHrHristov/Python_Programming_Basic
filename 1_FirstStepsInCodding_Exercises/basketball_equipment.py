annual_basketball_tax = int(input())

#Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

sneakers_price = annual_basketball_tax * 0.6
basketball_clothes = sneakers_price * 0.8
baskeball_ball = basketball_clothes / 4
basketball_accesoaries = baskeball_ball / 5

total_equipment = sneakers_price + basketball_clothes + baskeball_ball + basketball_accesoaries

total_sum = annual_basketball_tax + total_equipment

print(total_sum)
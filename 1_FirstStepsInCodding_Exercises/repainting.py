quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
working_hours = int(input())

nylon_price_per_sqm = 1.50
paint_price_per_l = 14.50
thinner_price_per_l = 5.00
bags_price_total = 0.40

#За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон,
# разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа,
# е равна на 30% от сбора на всички разходи за материали.

total_nylon_quantity = quantity_nylon + 2
total_paint_quantity = quantity_paint * 1.1

total_nylon_amount = total_nylon_quantity * nylon_price_per_sqm
total_paint_amount = total_paint_quantity * paint_price_per_l
total_thinner_amount = quantity_thinner * thinner_price_per_l
total_bags_amount = bags_price_total

amount_for_materials = total_bags_amount + total_thinner_amount + total_paint_amount + total_nylon_amount
amount_for_workers = working_hours * amount_for_materials * 30/100

final_result = round(amount_for_materials + amount_for_workers, 2)

print(final_result)

vegetables_price = float(input())
fruits_price = float(input())
vegetables_weight = int(input())
fruits_weight = int(input())

total_incomes = (vegetables_price * vegetables_weight) + (fruits_price * fruits_weight)
total_incomes_eur = total_incomes / 1.94
print(f'{total_incomes_eur:.2f}')


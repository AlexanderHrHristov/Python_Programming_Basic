deposit_sum = float(input())
months = int(input())
percent_of_interest = float(input())

interest = deposit_sum * percent_of_interest / 100
per_month = interest / 12
result = deposit_sum + per_month * months

print(float(result))

# Read user input
n = int(input())

# Logic
left_sum = 0
right_sum = 0

for i in range(n):
    num = int(input())
    left_sum += num
for i in range(n):
    num = int(input())
    right_sum += num

# Print output
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    if left_sum > right_sum:
        diff = left_sum - right_sum
    else:
        diff = right_sum - left_sum
    print((f"No, diff = {diff}"))

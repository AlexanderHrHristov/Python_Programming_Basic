n = int(input())
combination_counter = 0
for x1 in range (0, n + 1):
    for x2 in range (0, n + 1):
        for x3 in range (0, n + 1):
                x1 + x2 + x3 == n
                combination_counter += 1
print(f'{x1} + {x2} + {x3} = {n}')

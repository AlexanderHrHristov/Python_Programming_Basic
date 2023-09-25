# Read user input

from math import pi

figure = input()

# Logic

if figure == 'square':
    a = float(input())
    area = a ** 2

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif figure == 'circle':
    r = float(input())
    area = pi * r ** 2

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = (a * h) /2
# Print user input

print(f'{area:.3f}')
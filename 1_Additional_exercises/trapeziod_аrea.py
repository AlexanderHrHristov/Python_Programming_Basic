side_b1 = float(input())
side_b2 = float(input())
height = float(input())

area = (side_b1 + side_b2) * height / 2

# rounded_area = round(area, 2)
# print("{:.2f}".format(rounded_area))
#or
# print(f'{area:,.2f}')

print(f'{area:,.2f}')

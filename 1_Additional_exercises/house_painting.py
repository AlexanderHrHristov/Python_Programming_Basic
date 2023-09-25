house_height = float(input())
house_lenght = float(input())
roof_height = float(input())

house_area = (house_height ** 2) * 2 + (house_lenght * house_height) * 2
window_area = 2 * 1.5 * 1.5
door_area = 2 * 1.2
net_house_area = house_area - (window_area + door_area)
roof_area = (house_lenght * house_height) * 2 + (house_height * roof_height / 2) * 2

needed_green_paint = net_house_area / 3.4
needed_red_paint = roof_area / 4.3

print(f'{needed_green_paint:.2f}')
print(f'{needed_red_paint:.2f}')

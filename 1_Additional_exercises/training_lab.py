lab_lenght = float(input())
lab_width = float(input())

lenght_desks = lab_lenght // 1.2

number_of_width_desk = (lab_width - 1) // 0.7

total_desks = lenght_desks * number_of_width_desk - 3

print(f'{total_desks:.0f}')
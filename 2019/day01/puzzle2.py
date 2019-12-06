def fuel_needed_for_module(mass):
    fuel_needed = (mass//3) - 2
    if fuel_needed <= 0:
        return 0
    else:
        return fuel_needed + fuel_needed_for_module(fuel_needed)

with open('input.txt') as file:
    sum = 0
    for line in file:
        sum = sum + fuel_needed_for_module(int(line))
    print(sum)

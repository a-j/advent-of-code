def fuel_needed_for_module(mass):
    return (mass//3) - 2

with open('input.txt') as file:
    sum = 0
    for line in file:
        sum = sum + fuel_needed_for_module(int(line))
    print(sum)
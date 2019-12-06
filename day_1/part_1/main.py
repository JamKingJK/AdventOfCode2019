import math


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    total_required_fuel = 0
    for line in lines:
        module_mass = int(line)
        required_fuel = math.floor(module_mass / 3) - 2
        total_required_fuel += required_fuel
    print(total_required_fuel)

import math


def get_fuel_amount(mass):
    return math.floor(mass / 3) - 2


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    total_required_fuel = 0
    for line in lines:
        module_mass = int(line)
        required_fuel = get_fuel_amount(module_mass)
        total_required_fuel += required_fuel

        while True:
            required_fuel = get_fuel_amount(required_fuel)
            if required_fuel <= 0:
                break
            total_required_fuel += required_fuel

    print(total_required_fuel)

# https://adventofcode.com/2019/day/1

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

import math

def fuelRequired(mass):
    fuel = math.floor(mass / 3) - 2

    if fuel > 0:
        fuel = fuel + fuelRequired(fuel)
    else:
        return 0

    return fuel

# read input into list
with open('day1.2-input.txt') as f:
    spaceship = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
spaceship = [int(x.strip()) for x in spaceship]

# iterate and sum the fuel
totalFuel = 0

for module in spaceship:
    totalFuel = totalFuel + fuelRequired(module)

print(totalFuel)
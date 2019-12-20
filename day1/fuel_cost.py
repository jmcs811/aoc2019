import math
 
total_fuel = 0
need_fuel = 0
infile = open('input.txt', 'r')
 
def compute_fuel_cost(mass):
    '''
    recursive method to compute the fuel cost
    for the fuel cost for the fuel....
    '''
    if (math.trunc(mass / 3) - 2 <= 0):
        return 0
    # divide mass by 3, round down and sub 2
    fuel_cost = math.trunc(mass / 3)
    fuel_cost = fuel_cost - 2
    print(fuel_cost)
    return fuel_cost + compute_fuel_cost(fuel_cost)
 
for line in infile:
    total_fuel = total_fuel + compute_fuel_cost(int(line))
 
print(total_fuel)
import math
radius = float(input('Enter the radius of the circle: '))

def approximate_pi() :
    next_addition = math.sqrt(2)
    result = next_addition / 2

    while (math.sqrt(2 + next_addition) / 2) != 1 :
        result = result * math.sqrt(2 + next_addition) / 2
        next_addition = math.sqrt(2 + next_addition)

    pi = 2 / result
    return pi


def calculate_area(radius_parameter) :
    pi = approximate_pi()
    area = pi * radius_parameter * radius_parameter
    return area


print('The area is: ' + str(round(calculate_area(radius), 3)))
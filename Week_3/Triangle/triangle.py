import math

side_1 = float(input('Enter the length of the first side'))
side_2 = float(input('Enter the length of the second side'))
side_3 = float(input('Enter the length of the third side'))

def calculate_area(side1, side2, side3) :
    # FIRST, WE CALCULATE THE semi_perimeter (WHICH IS HALF THE PERIMETER)
    semi_perimeter = (side1 + side2 + side3) / 2

    # THEN WE USE THE SEMI PERIMETER TO CALCULATE THE AREA
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    return area

print(calculate_area(side_1, side_2, side_3))



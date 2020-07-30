w1 = int(input('enter 1st width'))
w2 = int(input('enter 2nd width'))
h1 = int(input('enter 1st height'))
h2 = int(input('enter 2nd height'))

def calculate_perimeter(w1, w2, h1, h2) :
    # PERIMETER IS = SIDE + SIDE + SIDE + SIDE....
    return w1 + w2 + h1 + h2

def calculate_price(perimeter) :
    # SINCE 1 METER IS R3, WE MULTIPLY THE TOTAL PERIMETER BY 3 FOR THE TOTAL PRICE
    return perimeter * 3

perimeter = calculate_perimeter(w1, w2, h1, h2)
price = calculate_price(perimeter)

print('the perimeter is: ' + str(perimeter) + 'meters, and the total price is: R' + str(price))

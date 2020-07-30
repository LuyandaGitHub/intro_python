print('choose a math operator')
print('+ for addition')
print('- for subtraction')
print('* for multiplication')
print('/ for division')
operation = input('Please enter the operation you want:')

# HERE WE CONVERT THE INPUTS FROM STRINGS TO FLOATS
number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter another number: '))

# IF THE CHOSEN OPERATOR IS +, THEN ADD THE TWO NUMBERS
if operation == '+':
    print(number_1 + number_2)

# IF THE CHOSEN OPERATOR IS -, THEN SUBTRACT THE TWO NUMBERS
elif operation == '-':
    print(number_1 - number_2)

# IF THE CHOSEN OPERATOR IS *, THEN MULTIPLY THE TWO NUMBERS
elif operation == '*':
    print(number_1 * number_2)

# IF THE CHOSEN OPERATOR IS /, THEN DIVIDE THE TWO NUMBERS
elif operation == '/':
    print(number_1 / number_2)

else:
    print('Invalid operator')




# operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
#
# number_1 = int(input('Enter your first number: '))
# number_2 = int(input('Enter your second number: '))
#
# if operation == '+':
#     print('{} + {} = '.format(number_1, number_2))
#     print(number_1 + number_2)
#
# elif operation == '-':
#     print('{} - {} = '.format(number_1, number_2))
#     print(number_1 - number_2)
#
# elif operation == '*':
#     print('{} * {} = '.format(number_1, number_2))
#     print(number_1 * number_2)
#
# elif operation == '/':
#     print('{} / {} = '.format(number_1, number_2))
#     print(number_1 / number_2)
#
# else:
#     print('You have not typed a valid operator, please run the program again.')
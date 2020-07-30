# PROGRAM TO GUESS A SECRET NUMBER
# LUYANDA DINGINDLELA
# 13 MAY 2020

# IMPORT A MODULE THAT GIVES RANDOM NUMBERS
from random import randint
secret_number = randint(0, 50)
users_guess = 0

# AS LONG AS WE HAVEN'T FOUND THE SECRET NUMBER, DO THIS
while users_guess != secret_number :
    # GET A NEW INPUT FROM THE USER
    users_guess = int(input('guess the number'))

    # CHECK IF THE GUESS IS TOO LOW
    if users_guess < secret_number :
        print('thats a bit low, try again')
    elif users_guess > secret_number :
        print('thats a bit too high, try again')
    else :
        print('thats correct!!')


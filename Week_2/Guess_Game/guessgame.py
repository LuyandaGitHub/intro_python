# IMPORT A MODULE THAT GIVES RANDOM NUMBERS
from random import randint

# SAVE SECRET WORDS IN A DICTIONARY SO THEY CAN BE USED
secret_words = {
    0: 'flash',
    1: 'batman',
    2: 'captain america',
    3: 'black panther',
    4: 'black lightning',
    5: 'superman',
    6: 'wonder women',
    7: 'black Widow',
    8: 'spiderman',
    9: 'deadpool',
    10: 'dare devil'
}

# SET THE AMOUNT OF LIVES TO 5
lives = 5

# SET THE SCORE TO 0
score = 0

while lives >= 0 :
    # HERE A RANDOM WORD IS CHOSEN FROM THE DICTIONARY USING THE randint FUNCTION
    word_to_guess = secret_words[randint(0, 10)]

    # GET THE USER INPUT THEN CHANGE THE IT TO LOWERCASE TO MATCH WITH THE VALUES IN THE DICTIONARY
    users_guess = input('Guess the hero').lower()

    if users_guess != word_to_guess :
        print('sorry, thats not it')
        lives = lives - 1
        print('you have ' + str(lives) + ' lives left')
    else :
        print('thats correct')
        score = score + 1
        print('your score is ' + str(score))
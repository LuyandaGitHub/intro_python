# IMPORT THE random MODULE
import random

# WE GOTTA CREATE A PASSWORD GENERATOR
# PASSWORD MUST BE AT LEAST 8 CHARACTERS
# MUST CONTAIN AT LEAST 1 UPPERCASE CHARACTER [A - Z]
# MUST CONTAIN AT LEAST 1 LOWERCASE CHARACTER [a - z]
# MUST CONTAIN AT LEAST 1 NUMBER [0 - 9]
# MUST CONTAIN AT LEAST 1 SPECIAL CHARACTER [! - &]


def generate_password() :
    uppercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lowercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_characters = ['!', '@', '#', '$', '%', '&', '^', '*', '(', ')', '?', '/']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # THE random.choice(list) FUNCTION GOES TO THE LIST IN ITS PARAMETERS(list) AND RETURNS A RANDOM CHARACTER FROM THE LIST
    password = random.choice(uppercase_characters) + random.choice(lowercase_characters) + random.choice(special_characters) + random.choice(uppercase_characters) + random.choice(uppercase_characters) + random.choice(numbers) + random.choice(uppercase_characters) + random.choice(special_characters) + random.choice(uppercase_characters) + random.choice(lowercase_characters) + random.choice(special_characters)
    return password

print('your password is: ' + generate_password())
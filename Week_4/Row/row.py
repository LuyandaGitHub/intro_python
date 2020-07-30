# GET THE INPUT FROM THE USER AND COVERT THE DATA TYPE TO AN INTERGER
starting_number = int(input('Enter the start number:'))

# INITIALISE A VARIABLE THAT WILL CONTAIN THE LIST OF NUMBERS
result = ''

# CHECK IF THE starting_number IS MORE THAN -6 BUT ALSO LESS THAN 93
if(-6 < starting_number < 93) :
  # MAKE A LOOP THAT RUNS 7 TIMES
  for i in range(7) :
    # NOW WE CONCATENATE THE RESULT AND THE STARTING NUMBER TOGETHER TO FORM THE FINAL ANSWER WHICH WOILL BE PRINTED
    result = str(result) + str(starting_number) + ' '
    # WE INCREASE THE STARTING NUMBER SO THAT IT ISN'T THE SAME ON EACH ITERATION
    starting_number = starting_number + 1

  print(result)
# HERE WE HANDLE ERRORS SO THAT IF THE starting_number DOESN'T MEET THE CONDITIONS, WE LET THE USER KNOW.
else :
  print('Your input is invalid')
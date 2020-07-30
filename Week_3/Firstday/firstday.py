# THIS LIST WILL BE USED TO PRINT THE DAYS
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# GET THE USERS INPUT AND CONVERT THE DATA TYPES FROM STRING TO INTEGERS
year_1 = int(input('Enter a year: '))
year_2 = int(input('Enter 2nd year'))


def get_first_day(year_parameter):
    # FORMULA TO CALCULATE THE FIRST DAY IN A GIVEN YEAR
    # A = year
    # R IS THE REMAINDER LEFT OVER
    # R(1 + 5R(A - 1, 4) + 4R(A - 1, 100) + 6R(A - 1, 400), 7)
    # BREAK UP THE MAIN FORMULA SO ITS EASIER TO WORK WITH
    equation_1 = (year_parameter - 1 % 4)
    equation_2 = (year_parameter - 1 % 100)
    equation_3 = (year_parameter - 1 % 400)

    # WE GET BACK A NUMBER THAT WE USE TO REFERENCE THE days_of_the_week LIST
    days_index = ((1 + 5 * equation_1 + 4 * equation_2 + 6 * equation_3) % 7)

    # NOW WE GET THE DAYS NAME FROM THE LIST
    return days_index - 2


# HERE WE GET THE DISTANCE BETWEEN THE TWO GIVEN YEARS
def get_distance_between_years(year_1_parameter, year_2_parameter):
    if(year_1_parameter > year_2_parameter) :
        distance_between_years = year_1_parameter - year_2_parameter
    else :
        distance_between_years = year_2_parameter - year_1_parameter

    return distance_between_years


distance = get_distance_between_years(year_1, year_2)

# THIS LOOP WILL PRINT OUT THE FINAL ANSWERS
if(year_1 > year_2) :
    while(distance != -1) :
        # EACH TIME THE LOOP HAPPENS, year_1 WILL BE DIFFERENT SO WE GET EACH 1ST DAY
        print('The 1st of January in ' + str(year_1) + ' was on a ' + days_of_the_week[get_first_day(year_1)])

        # WE DECREASE year_1 FOR THE NEXT ITERATION
        year_1 = year_1 - 1

        # WE DECREASE DISTANCE FOR THE NEXT ITERATION
        distance = distance - 1
else :
    while(distance >= 0) :
        # EACH TIME THE LOOP HAPPENS, year_2 WILL BE DIFFERENT SO WE GET EACH 1ST DAY
        print('The 1st of January in ' + str(year_2) + ' was on a ' + days_of_the_week[get_first_day(year_2)])

        # WE DECREASE year_1 FOR THE NEXT ITERATION
        year_2 = year_2 - 1

        # WE DECREASE DISTANCE FOR THE NEXT ITERATION
        distance = distance - 1

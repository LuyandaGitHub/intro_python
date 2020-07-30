# GET THE YEAR TO CHECK
year_input = int(input('Enter a year: \n'))
# GET THE MONTH TO CHECK
month_input = int(input('Enter a month number(1, ..., 12): \n'))

# THIS FUNCTION WILL TAKE AN INPUT AND DETERMINE WHETHER IT IS A LEAP YEAR OR NOT
def determine_leap_year(year_param) :
  # A LEAP YEAR HAPPENS EVERY 4 YEARS, BUT NOT EVERY 100 YEARS AND AGAIN EVERY 400 YEARS
  if(year_param % 4 == 0 and year_param % 100 != 0 or year_param % 400 == 0) :
    # print(str(year_param) + ' is a leap year. ')
    return True
  else : 
    # print(str(year_param) + ' is not a leap year.')
    return False


# THIS FUNCTION WILL TAKE AN INPUT AND RETURN THE MONTHS NAME
def determine_month(month_param) : 
  months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

  # THIS WILL CHECK IF month_param IS BETWEEN 1 - 12 TO ENSURE THAT THE USERS INPUT IS VALID 
  while(month_param not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) :
    month_param = int(input('Invalid input, please enter a month(1, ..., 12): \n'))

  # THE USER WILL ENTER A NUMBER BETWEEN 1 - 12, BUT SINCE INDEXES START AT 0, WE HAVE TO MINUS 1
  month_index = month_param - 1
  # print(str(months_list[month_index]) + ' is month number ' + str(month_param))

  # RETURN THE month_index WHICH WILL HELP IN THE determine_days_in_month()
  return month_index


# THIS FUNCTION TAKES IN A YEAR AND A MONTH NUMBER(1 - 12) AND RETURNS THE AMOUNT OF DAYS IN THAT MONTH 
def determine_days_in_month(month_param, year_param) :
  month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  month_days_list_on_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # CHECK IF THE year_param IS A LEAP YEAR OR NOT
  if(determine_leap_year(year_param)) :
    # SINCE determine_month() RETURNS THE month_index, WE CAN USE THAT TO DETERMINE HOW MANY DAYS THERE ARE IN THE GIVEN MONTH. THE month_index AND THE INDEX OF THE amount_of_days_in_month ARE THE SAME
    # EG. IF month_index = 2, THEN THE INDEX month_days_list[2] MATCHES months_list[2]
    amount_of_days_in_month = month_days_list_on_leap_year[determine_month(month_param)]
  else :
    amount_of_days_in_month = month_days_list[determine_month(month_param)]

  print('There are ' + str(amount_of_days_in_month) + ' amount of days in ' + str(month_input))


def determine_first_day_of_year(year_param):
  days_list = ['Sunday', 'Monday', 'Tuesaday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  # USE GAUS'S FORMULA TO CALCULATE THE FIRST DAY IN A GIVEN YEAR
  day_index = (1 + (year_param - 1) % 4 * 5 + (year_param - 1) % 100 * 4 + (year_param - 1) % 400 * 6) % 7

  return days_list[day_index]



# # THIS WILL KEEP TRACK OF THE CURRENT MONTH IN THE LOOP
# index = 0
# result = ''
# days_in_month = 0
# starting_number = 1
# months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# month_input = input('Enter the month(January, ...,December\n').lower()
# day_input = input('Enter the day(Monday, ...,Sunday\n').lower()

# # HERE, WE LOOP THROUGH THE months_list TO FIND WHICH MONTH MATCHES WITH M=THE MONTH THAT WAS INPUT
# for month in months_list :
 
#   # THIS CHECKS IF THE month_input IS EQUAL TO THE CURRENT month  
#   if(month_input == month) :
    
#     #THIS IS USED TO DECIDE HOW MANY DAYS IN THE YEAR THERE ARE 
#     if(index % 2 == 0) :
#       days_in_month = 30
#     else :
#       days_in_month = 31
#       if(month == 'january') :
#         days_in_month = 28


#     # THE AMOUNT OF TIMES WE LOOP WILL BE EQUAL TO THE days_in_month VARIABLE
#     while(starting_number < days_in_month) :
#       print(days_in_month)
      
#       # THIS WILL PRINT EACH ROW
#       for i in range(7) :
#         if(day_input == 'tuesday') :
#           result = ' ' 
#         elif(day_input == 'wednesday') :
#           result = ' ' + ' '
#         elif(day_input == 'thursday') :
#           result = ' ' + ' ' + ' '
#         elif(day_input == 'friday') :
#           result = ' ' + ' ' + ' ' + ' '
#         elif(day_input == 'saturday') :
#           result = ' ' + ' ' + ' ' + ' ' + ' '
#         elif(day_input == 'sunday') :
#           result = ' ' + ' ' + ' ' + ' ' + ' ' + ' '        
#         # NOW WE CONCATENATE THE RESULT AND THE STARTING NUMBER TOGETHER TO FORM THE FINAL ANSWER WHICH WOILL BE PRINTED
#         result = str(result) + str(starting_number) + ' '

#         if(starting_number != days_in_month) :
#           # WE INCREASE THE STARTING NUMBER SO THAT IT ISN'T THE SAME ON EACH ITERATION
#           starting_number = starting_number + 1
#         else :
#           starting_number = starting_number

#       # HERE, WE PRINT result WHICH, AT THIS POINT HAS 7 NUMBERS IN IT
#       print(result)
#       print(starting_number)

#       # NOW, WE RESET result SO WE CAN PRINT THE NEXT SEQUENCE OF NUMBERS
#       result = ''
#   else :
#     # IF THE CURRENT MONTH DOESN'T MATCH THE month_input, ICREASE index BY 1 
#     index = index + 1






































# GET THE MONTH INPUT
# GET THE DAY INPUT

# LOOP THROUGH THE months_list AND FIND WHERE THE month_input == CURRENT MONTH
  # GET THE CURRENT MONTH
  # GET THE CURRENT MONTH
  # DETERMINE HOW MANY DAYS THERE ARE IN THAT MONTH
  # USE THAT NUMBER AS THE RANGE TO LOOP
  # FIRST, WE GOTTA CHECK IF THERE ARE ANY SPACES THAT MUST BE PINTED
    # INSIDE THIS LOOP, HAVE ANOTHER LOOP THAT RUNS 7 TIMES

      # EG , MON TEU WED THU FRI SAT SUN
      #              1   2   3   4   5
      # THEN WE PRINT THE SEQUENCE OF DAYS
      # EG , MON TEU WED THU FRI SAT SUN
      #      1   2   3   4   5   6   7








index = 0
result = ''
days_in_month = 0
starting_number = 1
months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# GET THE MONTH INPUT
month_input = input('Enter the month(January, ...,December\n').lower()

# GET THE DAY INPUT
day_input = input('Enter the day(Monday, ...,Sunday\n').lower()

# LOOP THROUGH THE months_list AND FIND WHERE THE month_input == CURRENT MONTH
for month in months_list :
  
  # GET THE CURRENT MONTH
  if(month_input == month) :

    # DETERMINE HOW MANY DAYS THERE ARE IN THAT MONTH
    if(index % 2 == 0) :
      days_in_month = 30
    else :
      days_in_month = 31
      if(month == 'january') :
        days_in_month = 28
    
    # PRINT THE DAYS OF THE WEEK
    print('Mon Tue Wed Thu Fri Sat Sun')

    # FIRST, WE GOTTA CHECK IF THERE ARE ANY SPACES THAT MUST BE PINTED
    if(day_input == 'tuesday') :
      result = ' ' 
    elif(day_input == 'wednesday') :
      result = ' ' + ' '
    elif(day_input == 'thursday') :
      result = ' ' + ' ' + ' '
    elif(day_input == 'friday') :
      result = ' ' + ' ' + ' ' + ' '
    elif(day_input == 'saturday') :
      result = ' ' + ' ' + ' ' + ' ' + ' '
    elif(day_input == 'sunday') :
      result = ' ' + ' ' + ' ' + ' ' + ' ' + ' ' 

    # USE THAT NUMBER AS THE RANGE TO LOOP
    while(days_in_month >= 0) :
      print('result is ' + result + '.')    
      # INSIDE THIS LOOP, HAVE ANOTHER LOOP THAT RUNS 7 TIMES
      for i in range(7) :
        result = str(result) + str(starting_number) + ' '
        starting_number = starting_number + 1
        days_in_month = days_in_month - 1

      print(result)
      result = ''
  else :
    index = index + 1      
      
    

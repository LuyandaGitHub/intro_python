# FIRST, WE GET THE USERS INPUT IN THE FORM OF A INTERGER
hours = int(input('Enter the hours'))
minutes = int(input('Enter the minutes'))
seconds = int(input('Enter the seconds'))

# NOW, WE CHECK IF THE INPUT VALUES ARE VALID
if(hours < 0 or hours > 24) :
    print('Hour input is invalid')
elif(minutes < 0 or minutes > 60) :
    print('Minutes input is invalid')
elif(seconds < 0 or seconds > 60) :
    print('Seconds input is invalid')
else :
    # ONCE EVERYTHING CHECKS OUT, PRINT THE FOLLOWING
    print(str(hours) + ' hours, ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds')

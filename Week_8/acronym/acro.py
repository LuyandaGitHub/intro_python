def get_acronym() :
    # SO WE GET THE USERS INPUT BUT ALSO GET RID OF THE COMMA
    ignore_list = input('Please input the words to ignore, separated by a comma(the, for, and)\n').lower().replace(' ', '').split(',')
    title_list = input('Enter a title to generate its acronym').split()
    result = ''

    # FIRST, WE LOOP THROUGH THE title_list TO ACCESS EACH word INSIDE
    for word in title_list:
        # IF THE word ISN'T IN THE ignore_list, THEN...
        if word not in ignore_list:
            # WE CAPITALISE THE FIRST LETTER AND ADD IT TO THE result STRING
            result = result + word[0].upper()

    print(result)


get_acronym()
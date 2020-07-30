# THIS FUNCTION WILL PUSH THE SQUARES TO THE RIGHT
def push_right(grid_param):
    # LOOP THROUGH THE grid_param ARRAY
    for i in range(len(grid_param)):
        # SEPARATE THE grid_param INTO ROWS
        if(i % 4 == 0):
            new_row = []
            zeros_list = []
            filtered_row = []

            # CONVERT THE STRINGS TO NUMBERS
            first_square = int(grid_param[i])
            second_square = int(grid_param[i + 1])
            third_square = int(grid_param[i + 2])
            fourth_square = int(grid_param[i + 3])

            # CREATE AN ARRAY CONSISTING OF EACH SQUARE IN THE ROW
            row = [first_square, second_square, third_square, fourth_square]

            # LOOP THROUGH THE row AND CREATE AN ARRAY WITH THE NUMBERS THAT ARE > 0
            for square in row:
                if(square != 0):
                    filtered_row.append(square)

            # HERE, WE FIND OUT HOW MANY 0'S THERE ARE
            amount_of_zeros = 4 - len(filtered_row)

            # ADD 0'S TO THE zerosList
            for j in range(amount_of_zeros):
                zeros_list.append(0)

            # SINCE WE ARE PUSHING EVERYTHING RIGHT, WE START WITH zerosList INSTEAD OF THE filtered Row TO GET THE CORRECT ORDER
            for zero in zeros_list:
                new_row.append(zero)

            for number in filtered_row:
                new_row.append(number)

            # UPDATE THE grid_param BOARD
            grid_param[i] = new_row[0]
            grid_param[i + 1] = new_row[1]
            grid_param[i + 2] = new_row[2]
            grid_param[i + 3] = new_row[3]

    return grid_param


# THIS FUNCTION WILL PUSH THE SQUARES TO THE LEFT
def push_left(grid_param):
    # LOOP THROUGH THE grid_param ARRAY
    for i in range(len(grid_param)):
        # SEPARATE THE grid_param INTO ROWS
        if(i % 4 == 0):
            new_row = []
            zeros_list = []
            filtered_row = []

            # CONVERT THE STRINGS TO NUMBERS
            first_square = int(grid_param[i])
            second_square = int(grid_param[i + 1])
            third_square = int(grid_param[i + 2])
            fourth_square = int(grid_param[i + 3])

            # CREATE AN ARRAY CONSISTING OF EACH SQUARE IN THE ROW
            row = [first_square, second_square, third_square, fourth_square]

            # LOOP THROUGH THE row AND CREATE AN ARRAY WITH THE NUMBERS THAT ARE > 0
            for square in row:
                if(square != 0):
                    filtered_row.append(square)

            # HERE, WE FIND OUT HOW MANY 0'S THERE ARE
            amount_of_zeros = 4 - len(filtered_row)

            # ADD 0'S TO THE zerosList
            for j in range(amount_of_zeros):
                zeros_list.append(0)

            # SINCE WE ARE PUSHING EVERYTHING RIGHT, WE START WITH filtered_row INSTEAD OF THE zeros_list TO GET THE CORRECT ORDER
            # CREATE A NEW ROW THAT CONTAINS THE NEW POSITIONS OF THE SQUARES
            for number in filtered_row:
                new_row.append(number)

            for zero in zeros_list:
                new_row.append(zero)

            # UPDATE THE grid_param BOARD
            grid_param[i] = new_row[0]
            grid_param[i + 1] = new_row[1]
            grid_param[i + 2] = new_row[2]
            grid_param[i + 3] = new_row[3]

    return grid_param


# FUNCTION THAT'S GONNA PUSH THE SQUARES DOWN
def push_down(grid_param):
    # SEPARATE THE GRID INTO COLUMNS
    for i in range(4):
        new_column = []
        zeros_list = []
        filtered_column = []
        
        # CONVERT THE STRINGS TO NUMBERS
        first_square = int(grid_param[i])               # 0
        second_square = int(grid_param[i + 4])          # 4
        third_square = int(grid_param[i + (4 * 2)])     # 8
        fourth_square = int(grid_param[i + (4 * 3)])    # 12

        column = [first_square, second_square, third_square, fourth_square]

        # LOOP THROUGH THE row AND CREATE AN ARRAY WITH THE NUMBERS IN EACH ROW IF THE NUMBER IS > 0
        for square in column:
            if (square != 0):
                filtered_column.append(square)

        # HERE, WE FIND OUT HOW MANY 0'S THERE ARE
        amount_of_zeros = 4 - len(filtered_column)

        # ADD 0'S TO THE zerosList
        for j in range(amount_of_zeros):
            zeros_list.append(0)

        # SINCE WE ARE PUSHING EVERYTHING DOWN, WE START WITH zerosList INSTEAD OF THE filteredColumn TO GET THE CORRECT ORDER
        # CREATE A NEW COLUMN THAT CONTAINS THE NEW POSITIONS OF THE SQUARES
        for zero in zeros_list:
            new_column.append(zero)

        for number in filtered_column:
            if(filtered_column != []):
                new_column.append(number)

        # UPDATE THE grid_param BOARD
        grid_param[i] = new_column[0]
        grid_param[i + 1] = new_column[1]
        grid_param[i + 2] = new_column[2]
        grid_param[i + 3] = new_column[3]

    return grid_param


# FUNCTION THAT'S GONNA PUSH THE SQUARES UP
def push_up(grid_param):
    # SEPARATE THE GRID INTO COLUMNS
    for i in range(4):
        new_column = []
        zeros_list = []
        filtered_column = []

        # CONVERT THE STRINGS TO NUMBERS
        first_square = int(grid_param[i])               # 0
        second_square = int(grid_param[i + 4])          # 4
        third_square = int(grid_param[i + (4 * 2)])     # 8
        fourth_square = int(grid_param[i + (4 * 3)])    # 12

        column = [first_square, second_square, third_square, fourth_square];

        # LOOP THROUGH THE row AND CREATE AN ARRAY WITH THE NUMBERS IN EACH ROW IF THE NUMBER IS > 0
        for square in column:
            if (square != 0):
                filtered_column.append(square)

        # HERE, WE FIND OUT HOW MANY 0'S THERE ARE
        amount_of_zeros = 4 - len(filteredColumn)
#
        # ADD 0'S TO THE zerosList
        for j in range(amount_of_zeros):
            zeros_list.append(0)

        # SINCE WE ARE PUSHING EVERYTHING UP, WE START WITH filteredColumn INSTEAD OF THE zerosList TO GET THE CORRECT ORDER
        # CREATE A NEW COLUMN THAT CONTAINS THE NEW POSITIONS OF THE SQUARES
        for number in filtered_column:
            if(filtered_column != []):
                new_column.append(number)

        for zero in zeros_list:
            new_column.append(zero)

        # UPDATE THE grid_param BOARD
        grid_param[i] = new_column[0]
        grid_param[i + 1] = new_column[1]
        grid_param[i + 2] = new_column[2]
        grid_param[i + 3] = new_column[3]

    return grid_param
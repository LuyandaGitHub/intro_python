# IMPORT THE random MODULE
import random


# THIS FUNCTION WILL CREATE A GRID WITH 16 0'S
def create_grid(grid_param):
    for i in range(16):
        grid_param.append(0)


# THIS FUNCTION WILL PRINT THE GRID
def print_grid(grid_param):
    row_1 = ''
    row_2 = ''
    row_3 = ''
    row_4 = ''

    # WE LOOP THROUGH THE grid_param TO MAKE SURE WE GET EVERY ITEM INSIDE
    for j in range(len(grid_param)):
        if(j <= 3):
            row_1 += str(grid_param[j]) + ' | '
        elif(j > 3 and j < 8):
            row_2 += str(grid_param[j]) + ' | '
        elif(j > 7 and j < 12):
            row_3 += str(grid_param[j]) + ' | '
        elif(j > 11 and j < 16):
            row_4 += str(grid_param[j]) + ' | '

    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    
     
# THIS FUNCTION WILL GENERATE A RANDOM NUMBER
def generate_next_position(grid_param):
    # positionOfSquare WILL == A RANDOM NUMBER BETWEEN 0 AND THE LENGTH OF squares
    position_of_square = random.randint(0, len(grid_param) - 1)

    # CHECK IF positionOfSquare IS AVAILABLE
    if(grid_param[position_of_square] == 0):
        grid_param[position_of_square] = 2

        # CHECK IF GAME IS OVER
        check_for_loss(grid_param)
    else:
        # IF positionOfSquare IS UNAVAILABLE, RERUN THE generate_next_position()
        generate_next_position(grid_param)


# THIS FUNCTION IS GONNA COMBINE THE SQUARES
def merge_rows(grid_param):
    # WE USE squares.length, SO THAT WE DON'T CHECK THE SQUARE TO THE RIGHT OF THE LAST SQUARE
    for i in range(len(grid_param)):
        # MEANING SQUARES NEXT TO EACH OTHER ARE THE SAME
        if(grid_param[i] == grid_param[i + 1]):
            total = int(grid_param[i]) + int(grid_param[i + 1])

            # UPDATE THE grid_param
            grid_param[i] = total
            grid_param[i + 1] = 0

    checkForWin()


# THIS FUNCTION IS GONNA COMBINE THE SQUARES
def merge_columns(grid_param):
    # WE ARE CHECKING THE SQUARE BELOW THE ONE THAT WE 'RE LOOPING OVER. SO WE END AT 12 BECAUSE THERE ARE NO SQUARES UNDER SQUARE 13, 14, 15 AND 16
    for i in range(12):
        # MEANING SQUARES NEXT TO EACH OTHER ARE THE SAME
        if(grid_param[i] == grid_param[i + 4]):
            total = int(grid_param[i]) + int(grid_param[i + 4])
            # UPDATE THE grid_param
            grid_param[i] = total
            grid_param[i + 4] = 0

    checkForWin()


# THIS FUNCTION WILL CHECK FOR A WIN
def check_for_win(grid_param):
    for i in range(len(grid_param)):
        if(grid_param[i] == 2048):
            print('YOU WINN!!!!')


# THIS FUNCTION WILL CHECK FOR A LOSS
def check_for_loss(grid_param):
    zeros_amount = 0;

    for i in range(len(grid_param)):
        if(grid_param[i] == 0):
            zeros_amount = zeros_amount + 1

    if(zeros_amount == 0):
        print('YOU LOSE!!!')

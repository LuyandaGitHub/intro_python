# Import the os library which will be used to clear terminal after each move
import os

# IMPORTING util.py
import util

# IMPORTING push.py
import push


def play():
    grid = []

    # CREATE THE GRID
    util.create_grid(grid)

    # PLACE THE TWO NUMBERS ON THE BOARD
    util.generate_next_position(grid)

    while (True):
        # Clear the terminal so that the game seems more interactive
        os.system('cls' if os.name == 'nt' else 'clear')

        # PRINT THE CURRENT GRID
        util.print_grid(grid)

        # set 'key' to a user input which represents the move they would like to do
        key = input ("Enter a direction:\n")

        # check if 'key' is one of the available options
        if (key in ['x', 'u', 'd', 'l', 'r']):
            if (key == 'x'):
                # quit the game
                return
            # manipulate the grid depending on input
            elif (key == 'u'):
                grid = push.push_up(grid)
            elif (key == 'd'):
                grid = push.push_down(grid)
            elif (key == 'r'):
                grid = push.push_right(grid)
            elif (key == 'l'):
                grid = push.push_left(grid)

            print(grid)
            # check for a grid with no more gaps or legal moves
            util.check_for_loss(grid)
            util.check_for_win(grid)
# grid = []
#
# util.create_grid(grid)
#
# util.generate_next_position(grid)
# print('grid')
# print(grid)
# grid = push.push_left(grid)
# print(grid)
# print('                                                                                 ')
#
# # util.print_grid(grid)
# # print('                                                                                 ')
# #
# # print('                                                                                 ')
# #
# # util.print_grid(grid)






play()
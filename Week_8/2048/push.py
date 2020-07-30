# THIS FUNCTION MERGES BLOCKS UPWARDS
def push_up(board_param):
    # game_still_going WILL BE USED DO DETERMINE WHETHER THE LOOP SHOULD CONTINUE
    game_still_going = True

    while game_still_going:
        game_still_going = False

        # THIS WILL LOOP THROUGH THE board_param
        for col_i in range(4):
            # THIS WILL LOOP THROUGH THE LAST THREE NUMBERS IN THE COLUMN
            for num_i in range(1, 4):
                # CHECK IF THE NUMBER ON TOP OF THE ONE IS 0
                if board_param[num_i - 1][col_i] == 0:
                    if board_param[num_i][col_i] == 'x':
                        # CHANGE THIS TO AN X
                        board_param[num_i - 1][col_i] = 'x'

                    else:
                        # NOW WE LOOP FROM THE CURRENT NUMBER UNTIL THE LAST NUMBER OF THE COLUMN
                        for num_j in range(num_i, 4):
                            board_param[num_j - 1][col_i] = board_param[num_j][col_i]

                        board_param[num_j][col_i] = 'x'

                        # UPDATE game_still_going
                        game_still_going = True

    # LOOP THROUGH EACH COLUMN IN board_param
    for col_i in range(4):
        # THIS WILL LOOP THROUGH THE LAST THREE NUMBERS IN THE COLUMN
        for num_i in range(1, 4):
            if board_param[num_i - 1][col_i] == board_param[num_i][col_i] != 'x':
                board_param[num_i - 1][col_i] += board_param[num_i][col_i]
                # CHANGE THIS TO 0
                board_param[num_i][col_i] = 0

    game_still_going = True

    while game_still_going:
        game_still_going = False
        for col_i in range(4):
            for num_i in range(1, 4):
                if board_param[num_i - 1][col_i] == 0:
                    if board_param[num_i][col_i] == 'x':
                        board_param[num_i - 1][col_i] = 'x'
                    else:
                        for num_j in range(num_i, 4):
                            board_param[num_j - 1][col_i] = board_param[num_j][col_i]
                        board_param[num_j][col_i] = 'x'
                        game_still_going = True

    # NOW, WE LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH EACH NUMBER IN THE ROW
        for num_i in range(4):
            if board_param[row_i][num_i] == 'x':
                # REPLACE X'S WITH 0'S
                board_param[row_i][num_i] = 0


def push_down(board_param):
    # game_still_going WILL BE USED DO DETERMINE WHETHER THE LOOP SHOULD CONTINUE
    game_still_going = True

    while game_still_going:
        game_still_going = False
        # LOOP THROUGH EACH COLUMN
        for col_i in range(4):
            # LOOP THROUGH THE FIRST 3 NUMBERS
            for num_i in range(2, -1, -1):
                if board_param[num_i + 1][col_i] == 0:
                    if board_param[num_i][col_i] == 'x':
                        board_param[num_i + 1][col_i] = 'x'
                    else:
                        # LOOP FROM THE CURRENT NUMBER UNTIL THE FIRST NUMBER IN THE COLUMN
                        for num_j in range(num_i, -1, -1):
                            board_param[num_j + 1][col_i] = board_param[num_j][col_i]
                        board_param[num_j][col_i] = 'x'

                        game_still_going = True

    # LOOP THROUGH EACH COLUMN
    for col_i in range(4):
        # LOOP THROUGH THE FIRST 3 NUMBERS
        for num_i in range(2, -1, -1):
            if board_param[num_i + 1][col_i] == board_param[num_i][col_i] != 'x':
                board_param[num_i + 1][col_i] += board_param[num_i][col_i]

                # CHANGE THIS TO 0
                board_param[num_i][col_i] = 0

    game_still_going = True

    while game_still_going:
        game_still_going = False
        for col_i in range(4):
            for num_i in range(2, -1, -1):
                if board_param[num_i + 1][col_i] == 0:
                    if board_param[num_i][col_i] == 'x':
                        board_param[num_i + 1][col_i] = 'x'
                    else:
                        for num_j in range(num_i, -1, -1):
                            board_param[num_j + 1][col_i] = board_param[num_j][col_i]
                        board_param[num_j][col_i] = 'x'
                        game_still_going = True

    # LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH EACH NUMBER IN THE ROW
        for num_i in range(4):
            if board_param[row_i][num_i] == 'x':
                # REPLACE X WITH 0
                board_param[row_i][num_i] = 0


def push_right(board_param):
    # game_still_going WILL BE USED DO DETERMINE WHETHER THE LOOP SHOULD CONTINUE
    game_still_going = True

    while game_still_going:
        game_still_going = False

        # LOOP THROUGH EACH ROW
        for row_i in range(4):
            # LOOP THROUGH THE FIRST 3 NUMBERS IN THE ROW
            for num_i in range(2, -1, -1):
                if board_param[row_i][num_i + 1] == 0:
                    if board_param[row_i][num_i] == 'x':
                        board_param[row_i][num_i + 1] = 'x'
                    else:

                        # LOOP FROM THE CURRENT NUMBER UNTIL THE FIRST NUMBER IN THE ROW
                        for num_j in range(num_i, -1, -1):
                            board_param[row_i][num_j + 1] = board_param[row_i][num_j]

                        board_param[row_i][num_j] = 'x'
                        game_still_going = True

    # LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH THE FIRST 3 NUMBERS IN THE ROW
        for num_i in range(2, -1, -1):
            if board_param[row_i][num_i + 1] == board_param[row_i][num_i] != 'x':
                board_param[row_i][num_i + 1] += board_param[row_i][num_i]

                # CHANGE THIS TO 0
                board_param[row_i][num_i] = 0

    game_still_going = True

    while game_still_going:
        game_still_going = False
        for row_i in range(4):
            for num_i in range(2, -1, -1):
                if board_param[row_i][num_i + 1] == 0:
                    if board_param[row_i][num_i] == 'x':
                        board_param[row_i][num_i + 1] = 'x'
                    else:
                        for num_j in range(num_i, -1, -1):
                            board_param[row_i][num_j + 1] = board_param[row_i][num_j]
                        board_param[row_i][num_j] = 'x'
                        game_still_going = True

    # LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH EACH NUMBER IN THE ROW
        for num_i in range(4):
            if board_param[row_i][num_i] == 'x':
                # REPLACE X WITH
                board_param[row_i][num_i] = 0


def push_left(board_param):
    # game_still_going WILL BE USED DO DETERMINE WHETHER THE LOOP SHOULD CONTINUE
    game_still_going = True

    while game_still_going:
        game_still_going = False
        # LOOP THROUGH EACH ROW
        for row_i in range(4):
            # LOOP THROUGH THE LAST 3 NUMBERS IN THE ROW
            for num_i in range(1, 4):
                if board_param[row_i][num_i - 1] == 0:
                    if board_param[row_i][num_i] == 'x':
                        board_param[row_i][num_i - 1] = 'x'
                    else:
                        # LOOP FROM THE CURRENT NUMBER UNTIL THE LAST NUMBER IN THE ROW
                        for num_j in range(num_i, 4):
                            board_param[row_i][num_j - 1] = board_param[row_i][num_j]

                        board_param[row_i][num_j] = 'x'
                        game_still_going = True

    # LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH THE LAST 3 NUMBERS
        for num_i in range(1, 4):
            if board_param[row_i][num_i - 1] == board_param[row_i][num_i] != 'x':
                board_param[row_i][num_i - 1] += board_param[row_i][num_i]
                board_param[row_i][num_i] = 0

    game_still_going = True

    while game_still_going:
        game_still_going = False
        for row_i in range(4):
            for num_i in range(1, 4):
                if board_param[row_i][num_i - 1] == 0:
                    if board_param[row_i][num_i] == 'x':
                        board_param[row_i][num_i - 1] = 'x'
                    else:
                        for num_j in range(num_i, 4):
                            board_param[row_i][num_j - 1] = board_param[row_i][num_j]
                        board_param[row_i][num_j] = 'x'
                        game_still_going = True

    # LOOP THROUGH EACH ROW
    for row_i in range(4):
        # LOOP THROUGH EACH NUMBER IN THE ROW
        for num_i in range(4):
            if board_param[row_i][num_i] == 'x':
                # REPLACE X WITH
                board_param[row_i][num_i] = 0



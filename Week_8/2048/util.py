grid = []

def create_grid(grid_param):
    # FIRST WE CREATE THE inner_grid VARIABLE SO THAT WE CAN USE IT LATER
    inner_grid = []

    # THIS LOOP WILL RUN 4 TIMES
    for i in range(4) :
        # NOW, ON EACH ITERATION...WE APPEND 0 TO THE inner_grid
        inner_grid.append(0)

        # THEN WE APPEND inner_grid TO THE grid_param
        grid_param.append(inner_grid)


def print_grid(grid_param):
    result = ''

    # SO WE GOTTA LOOP FOR THE LENGTH OF grid_param AND GET EACH inner_grid
    for i in range(len(grid_param)):
        current_grid = grid_param[i]

        # NOW THAT WE ARE INSIDE THE LIST, WE CAN LOOP INSIDE THE inner_grid
        for j in range(len(current_grid)):
            # ON EACH ITERATION, WE CONCATENATE result WITH current_grid[j]
            result = result + str(current_grid[j]) + ' | '

        print(result)

        # HERE, WE RESET result SO THAT ITS EMPTY ON THE NEXT BIG ITERATION
        result = ''


def check_lost(grid_param):
    # THIS LOOP WILL GET US INSIDE THE grid_param
    for i in range(len(grid_param)):
        current_grid = grid_param[i]

        # NOW WE LOOP THROUGH THE inner_list
        for j in range(len(current_grid)):
            # HERE, WERE CHECKING IF THE inner_grids SQUARE IS == 0 OR IF j + 1 < THE LENGTH OF THE grid_param
            if (grid_param[i][j] == 0 or j + 1 < len(grid_param)):
                # NOW, WE CHECK IF THE CURRENT inner_grid's VALUE IS == THE CURRENT inner_grid's VALUE + 1
                if (grid_param[i][j] == grid_param[i][j + 1] or grid_param[j][i] == grid_param[j + 1][i]):
                    return False

    return True


def check_won(grid_param):
    # THIS LOOP WILL GET US INSIDE THE grid_param
    for i in range(len(grid_param)):
        current_grid = grid_param[i]

        # NOW WE LOOP THROUGH THE inner_list
        for j in range(len(current_grid)):
            try:
                # HERE, WERE CHECKING IF THE inner_grids SQUARE IS == 0 OR IF j + 1 < THE LENGTH OF THE grid_param
                if (current_grid[j] >= 32):
                   return False
            except:
                for item in current_grid[j]:
                    # HERE, WERE CHECKING IF THE inner_grids SQUARE IS == 0 OR IF j + 1 < THE LENGTH OF THE grid_param
                    if (item >= 32):
                        return False

    return True


def copy_grid(grid_param):
    copy_of_current_grid = []
    main_grid = grid_param[0]

    for row in  main_grid:
        copy_of_current_grid.append(row)

    return copy_of_current_grid


def grid_equal(grid_1_param, grid_2_param):
    # RETURN TRUE IF THEY ARE EQUAL, FALSE IF NOT
    return grid_1_param == grid_2_param










# create_grid(grid)Y


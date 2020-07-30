# CREATE THE EMPTY BOARD
winner = None
current_player = 'X'
game_still_going = True
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# THIS WILL DRAW THE BOARD BY PRINTNG board IN A SPECIFIC FORMAT
def render_board() :
  print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
  print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
  print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')


def play_a_turn(current_player_param) :
  # INPUT RETURNS A STRING SO WE CHANGE THE DATA TYPE SO WE CU=AN USE IT TO INDEX THROUGH THE board
  position_input = input(current_player_param + ', choose a position between 1 - 9\n')
  

  while(position_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']) :
    position_input = input('Invalid input ' + current_player_param + '. Choose a position between 1 - 9\n') 
  # THE USER CHOSE A NUMBER BETWEEN 1 - 9, BUT LISTS START FROM 0...MEANING WE HAVE TO MINUS 1 FROM position_input TO GET THE CORRECT INDEX
  position_on_board = int(position_input) - 1

  if(board[position_on_board] == '-') :
    # NOW WE UPDATE THE board
    board[position_on_board] = current_player_param
  else : 
    print('That spot has been taken already')

  # NOW WE SHOW THE board
  render_board()


def check_if_game_over() :
  check_for_winner()
  check_for_tie()


def check_for_winner() :
  # IF WE WANNA SET A GLOBAL VARIABLE, WE HAVE TO DECLARE IT INSIDE THE FUNCTION
  global winner

  # CHECK THE ROWS
  row_winner = check_rows()

  # CHECK THE COLUMNS
  column_winner = check_columns()
  
  # CHECK THE DIAGONALS
  diagonal_winner = check_diagonals()

  if(row_winner) :
    # THERE WAS A WIN ON ONE OF THE ROWS 
    winner = row_winner
  elif(column_winner) :
    # THERE WAS A WIN ON ONE OF THE COLUMNS 
    winner = column_winner
  elif(diagonal_winner) :
    # THERE WAS A WIN ON ONE OF THE DIAGONALS 
    winner = diagonal_winner
  else :
    # IN THIS CASE, THERE WAS NO WINNER
    winner = None


def check_rows() :
  # HERE, WE ARE ACCESSING THE GLOBAL VARIABLE game_still_going
  global game_still_going
  # THIS CHECKS IF board[0], board[1] AND board[2] HAVE THE SAME VALUE OR NOT. 
  # BECAUSE THE FIRST PART IS CHECKING IF THE VALUES ARE EQUAL, THE != '-' CHECKS IF THE VALUES ARE NOT EQUAL TO '-'
  # IF THEY DO, row_1 = True, IF NOT row_1! = False
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  # IF ANY ROW IS TRUE, THERE WAS A winner
  if(row_1 or row_2 or row_3) :
    game_still_going = False

  # WE KNOW THAT THERE WAS A WINNER, WE JUST DONT KNOW WHO WON, SO WE CHECK EACH ROW AND GET THE VALUE OF board ON EACH ROW WHIC WILL BE THE winner
  if(row_1) :
    return board[0]
  elif(row_2) :
    return board[3]
  elif(row_3) :
    return board[6]

  return 


def check_columns() :
  # HERE, WE ARE ACCESSING THE GLOBAL VARIABLE game_still_going
  global game_still_going
  # THIS CHECKS IF board[0], board[1] AND board[2] HAVE THE SAME VALUE OR NOT. 
  # BECAUSE THE FIRST PART IS CHECKING IF THE VALUES ARE EQUAL, THE != '-' CHECKS IF THE VALUES ARE NOT EQUAL TO '-'
  # IF THEY DO, column_1 = True, IF NOT column_1! = False
  column_1 = board[0] == board[3] == board[6] != '-'
  column_2 = board[1] == board[4] == board[7] != '-'
  column_3 = board[2] == board[5] == board[8] != '-'

  # IF ANY ROW IS TRUE, THERE WAS A winner
  if(column_1 or column_2 or column_3) :
    game_still_going = False

  # WE KNOW THAT THERE WAS A WINNER, WE JUST DONT KNOW WHO WON, SO WE CHECK EACH ROW AND GET THE VALUE OF board ON EACH ROW WHIC WILL BE THE winner
  if(column_1) :
    return board[0]
  elif(column_2) :
    return board[1]
  elif(column_3) :
    return board[2]

  return 


def check_diagonals() :
  # HERE, WE ARE ACCESSING THE GLOBAL VARIABLE game_still_going
  global game_still_going
  # THIS CHECKS IF board[0], board[1] AND board[2] HAVE THE SAME VALUE OR NOT. 
  # BECAUSE THE FIRST PART IS CHECKING IF THE VALUES ARE EQUAL, THE != '-' CHECKS IF THE VALUES ARE NOT EQUAL TO '-'
  # IF THEY DO, diagonal_1 = True, IF NOT diagonal_1! = False
  diagonal_1 = board[0] == board[4] == board[8] != '-'
  diagonal_2 = board[2] == board[4] == board[6] != '-'

  # IF ANY ROW IS TRUE, THERE WAS A winner
  if(diagonal_1 or diagonal_2) :
    game_still_going = False

  # WE KNOW THAT THERE WAS A WINNER, WE JUST DONT KNOW WHO WON, SO WE CHECK EACH ROW AND GET THE VALUE OF board ON EACH ROW WHIC WILL BE THE winner
  if(diagonal_1) :
    return board[0]
  elif(diagonal_2) :
    return board[2]

  return 


def check_for_tie() :
  # HERE, WE ARE ACCESSING THE GLOBAL VARIABLE game_still_going
  global game_still_going

  # IF THERE ISNT A SINGLE - IN THE WHOLE board LIST, THEN THE GAME IS OVER
  if('-' not in board) :
    game_still_going = False
  return


def switch_player() :
  # HERE, WE ARE ACCESSING THE GLOBAL VARIABLE current_player
  global current_player

  # IF cuurent_player IS X, THEN SWITCH TO O AND VICE VERSA
  if(current_player == 'X') :
    current_player = 'O'
  else : 
    current_player = 'X'


def play_game() :
  # FISRT THING TO DO IS DRAW THE BOARD
  render_board()

  # CHOOSE WHOS TURN IT IS
  while (game_still_going) :
    # NOW WE MUST DECIDE WHOS TURN IT IS
    play_a_turn(current_player)

    # NOW WE CHECK IF THE GAME IS STILL GOING ON BY LOOKING FOR WINNERS OR A TIE
    check_if_game_over()

    # NOW WE SWITCH PLAYERS
    switch_player()

  # AT THIS POINT, ITS GAME OVER. EITHER THE WAS A WINNER OR A TIE
  if(winner != None) :
    print('Yay, ' + winner + ' has won')
  elif(winner == None) :
    print('Its a tie!')


play_game()
# PRINTING RABBITS
# REMEMBER THAT BACKSLASHES ESCAPES CHARACTERS
# \n STARTS A NEW LINE

print('(\\ \\                                                       (\/)                        ')
print('( \' \')                     (\_/)                        (. .  )                        / /)')
print('O(\'\') (\'\')               (\ \'.\' /)                    (\'\') (\'\')O                     (\'\'  )')
print('                         (\'\')_(\'\')                                                   ( )( )O')

# CREATE SEPARATE FUNCTIONS TO DRAW EACH RABBIT SEPARATELY
def print_rabbit_left() :
    print('(\\ \\\n'
          '\n'
          '( \' \')\n'
          '\n'
          'O(\'\') (\'\')')

def print_rabbit_front() :
    print('   (\_/)  \n'
          '\n'
          '(\ \' . \' /) \n'
          '\n'
          ' (\'\')_(\'\')')

def print_rabbit_right() :
    print('     (\/)\n'
          '\n'
          '   (. . )\n'
          '\n'
          '(\'\') (\'\')O')

def print_rabbit_far_right() :
    print('  / /)\n'
          '\n'
          '(\'\'  )\n'
          '\n'
          '( )( )O')

# print_rabbit_left()
# print_rabbit_front()
# print_rabbit_right()
# print_rabbit_far_right()
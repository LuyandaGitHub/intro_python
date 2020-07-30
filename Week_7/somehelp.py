# IMPORTING THE random MODULE
import random

def welcome():
  print('Welcome to the automated technical support system.')
  print('Please describe your problem.')

def get_input():
  return input().lower()


def main():
  # responces_list CONTAINS A LIST OF POTENTIAL RESPONCES TO THE USER
  responces_list = [
    'Have you tried it on a different operating system?', 
    'Did you reboot it?', 'What color is it?', 
    'You should consider installing anti-virus software.', 
    'Contact Telkom', 
    'I would get that looked at if i were you'
  ]

  # CALLS welcome()
  welcome()

  # CALLS get_input()
  query = get_input()
  
  # WHILE THE USER HASNT TYPED IN quit
  while (not query=='quit'):
    # GET A RANDOM RESPONCE FROM THE responces_list
    print(responces_list[random.randint(0, 5)])

    query = get_input()    
  
  
main()


# THIS MAKES SURE THAT MAIN IS ONLY RUN WHEN CALLED AND NOT WHEN IMPORTED
if __name__ == '__main__': main()
def welcome():
  print('Welcome to the automated technical support system.')
  print('Please describe your problem.')

def get_input():
  return input().lower()


def get_responce(query_param) :
  # keyword_responses CONTAINS A LIST OF POTENTIAL RESPONCES TO THE USER
  keyword_responses = {
        'crashed' : 'Are the drivers up to date?',
        'blue'    : 'Ah, the blue screen of death. And then what happened?',
        'bluetooth' : 'Have you tried mouthwash?',
        'windows'  : 'Ah, I think I see your problem. What version?',
        'apple'    : 'You do mean the computer kind?',
        'spam'     : 'You should see if your mail client can filter messages.',
        'connection' : 'Contact Telkom.'
  }

  # HERE, WE LOOP THROUGH THE keyword_responses
  for key in keyword_responses:
    # IF THE query_param AND THE key MATCH, THEN...
    if(query_param == key) :
      # PRINT THE VALUE AT THAT KEY
      print(keyword_responses[key])


def main():
  # CALLS welcome()
  welcome()

  # CALLS get_input()
  query = get_input()
  
  # WHILE THE USER HASNT TYPED IN quit
  while (not query=='quit'):
    # CALL THE get_responce() AND PASS IN THE query, WHICH IS WHAT THE USER TYPED IN
    get_responce(query)

    query = get_input()
  
  
main()


# THIS MAKES SURE THAT MAIN IS ONLY RUN WHEN CALLED AND NOT WHEN IMPORTED
if __name__ == '__main__': main()
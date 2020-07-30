def welcome():
  print('Welcome to the automated technical support system.')
  print('Please describe your problem.')


def get_input():
  return input().lower()


def search_dictionary(query_param, dictionary_param):
  # HERE, WE CHECK IF THE query_param IS IN THE dictionary_param
  if(query_param in dictionary_param) :
    return dictionary_param[query_param]

    # IF NOT, THEN RETURN 'Curious, tell me more.'
  else :
    return 'Curious, tell me more.'



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

  # BREAK UP THE query_param TO A LIST 
  query_list = query_param.split()

  # NOW, WE LOOP THROUGH THE query_list TO CHECK EACH INDIVIDUAL WORD
  for item in query_list :
    # CHECK IF THE item IS IN THE keyword_responses DICTIONARY
    print(search_dictionary(item, keyword_responses))


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
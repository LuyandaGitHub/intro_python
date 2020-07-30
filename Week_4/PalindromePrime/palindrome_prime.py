start = int(input('Enter the start point'))
end = int(input('Enter the end point'))
palindrome_list = []

while(start < end) :
  start_string = str(start)
  reverse_string = start_string[::-1]

  if(start_string == reverse_string) :

    if(start > 1) :

      for i in range(2, start) :
    
        if((start % i) == 0) :
          break
        else :
          palindrome_list.append(start)

  start = start + 1



for i in range(len(palindrome_list)) :
  for j in range(len(palindrome_list)) :  
    if(palindrome_list[i] != palindrome_list[j]) :
      print(palindrome_list[i])
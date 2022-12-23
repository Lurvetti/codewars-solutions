def order(sentence):
  strings = sentence.split(' ')
  print("Old string: " + sentence)
    
  new = '' #init new string
  n = 1 #init for loop
  while (n <=9):
      for word in strings: #loop each word in splitted array
          if(str(n) in word): #find the number in each word
              new = new + ' ' + word #update new string
      n = n + 1 #iterate loop
  print("New ordered string: " + new[1:])
  return new[1:] #returning the correct string, withou the first ' '

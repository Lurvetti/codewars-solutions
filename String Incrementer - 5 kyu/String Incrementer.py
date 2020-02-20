def increment_string(string):
   head = string.rstrip('0123456789')
   tail = string[len(head):]
   
   if (tail != ''):
       number = int(tail) + 1
       print(number)
       tail = str(number).zfill(len(tail))
       print(tail)
       return head+tail
   return (string + '1')

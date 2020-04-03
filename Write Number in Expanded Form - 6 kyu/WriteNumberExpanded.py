def expanded_form(num):
    string = '' #start string
    zeros = len(str(num)) - 1 #get the initial number of 0s
    
    for digit in str(num): #loop each digit
        if(int(digit) != 0): #test if the number is not 0
            string = string +(str(digit)+('0'*zeros + ' + ')) #concatenate in the string
        zeros -= 1 #update zeros value
        
    return string[:-3] #return the correct str
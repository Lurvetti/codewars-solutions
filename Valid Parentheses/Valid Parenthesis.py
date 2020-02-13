def valid_parentheses(string):
    print(list(string))
    
    p = 0 #initial parenthesis control variable
    for char in list(string): #loop string
        if char == '(':
            p = p + 1
        if char == ")":
            p = p - 1
        if p == -1: #if there is a ')' not closed 
            return False
            
    if p != 0: #if there is a '(' not closed 
        return False
    else:
        return True #return if 0

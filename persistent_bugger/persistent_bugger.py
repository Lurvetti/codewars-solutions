def persistence(n):
    n_array = [n for n in str(n)] #make a new int array from
    print(n_array)
    pers = 0 #init pers
    
    while(len(n_array) > 1): #changing arrays unitl lenght is 1
        new = 1 #init new
        
        #multiply each number in the array for the new value
        for n in n_array:
            new = int(n) * new
        n_array = str(new) #update the array to be the result of multiplactions
        print(new)
        pers = pers + 1 #update pers
        
    return pers

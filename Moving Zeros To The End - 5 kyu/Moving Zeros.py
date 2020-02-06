def move_zeros(array):
    clean = [] #clean array
    z = 0 #zero count
    
    for el in array: #loop elements in array
        if((el is False and type(el) is bool) or (el != 0.0)): #test if not 0 or 0.0
            print (el)
            clean.append(el) #copy value
        else:
            z += 1 #it is 0 or 0.0, increment counter
    return clean + z*[0] #return combined array

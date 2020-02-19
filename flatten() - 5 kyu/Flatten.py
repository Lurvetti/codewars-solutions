def flatten(*args):
    print('Beggining:' + str(args))  
    
    #test if input has list and flag it
    haslist = False
    for elements in args:
        if(type(elements) == list):
            print('1if - has List')
            haslist = True
            break
    
    #if input has list
    if(haslist == True):
        new = []
        print('List does have another list')
        for elements in args: #loop elements
            if(type(elements) != list): #if not a list, just append
                new.append(elements)
            else: #if its a list, loop and append
                for el in elements:
                    if (el != []): #exclude
                        new.append(el)
        return(flatten(*new)) #recursive with new array

    #if there is no more list, return the array
    else:
        return (list(args))

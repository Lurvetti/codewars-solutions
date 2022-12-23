def unique_in_order(iterable):
    new = []
    last = None
    for i in list(iterable): #loop each value of the list
        if (i != last): #if is different from last value, append to new array
            print(i)
            new.append(i)
        last = i   
    return new

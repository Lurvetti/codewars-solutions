def kebabize(string):
    #remove digits
    kebab = [ch for ch in string if ch.isdigit() == False]
    
    #loop iterable
    for idx,ch in enumerate(kebab):
            if(ch.isupper()): #test for Uppercase
                kebab[idx] = ch.lower() #replace for lower
                if(idx>0): #insert '-' if not first char
                    kebab.insert(idx, '-')
        
    return ''.join(kebab)

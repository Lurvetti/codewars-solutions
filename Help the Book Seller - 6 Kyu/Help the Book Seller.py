def stock_list(listOfArt, listOfCat):
    
    #test for empy lists
    if(len(listOfArt) == 0 or len(listOfCat) == 0):
        return ''
    
    result = []
    for cat in listOfCat: #iterate categories
        sum = 0
        for art in listOfArt: #iterate art
            if(cat == list(art.split()[0])[0]): #test if art is from categories
                sum = sum + int(art.split()[1]) #sum the number of books
        result.append('('+cat+' : '+str(sum)+')'+' - ')     #update the result list   
        #print(result)
    
    return ''.join(result).strip(' - ') #returns formatted result string

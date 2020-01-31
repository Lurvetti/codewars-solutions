def generate_hashtag(s):    
    if(s == '' or len(s) > 140): #inital tests
        return False
    else:
        new = [word.capitalize() for word in s.split() if word != ''] #capitalize words and add to new list if not ''
        new = '#' + ''.join(new) #add '#' and join new list
        print('new') #print new to make sure it  is good
        return  (new) #return
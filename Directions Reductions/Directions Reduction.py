def dirReduc(arr):
    #dic with opposites
    dic = {"NORTH" : "SOUTH","SOUTH" : "NORTH", "EAST": "WEST", "WEST":"EAST"}
    
    #function for deleting
    def remove_ops(arr):
        print(arr) #print to see array evolution
        for idx, dir in enumerate(arr): #loop directions
            try: #this will make sure that we don't have a index problem
                if(dic[dir] == arr[idx+1]): #actual test
                    print('This will be deleted: ' + dir + ' ' + arr[idx+1])
                    del arr[idx:idx+2] #deletind
                    remove_ops(arr) #recursion
            except:
                return arr #if we reach the end (erro idx), return the final arr
    
    remove_ops(arr) #runs the function for the first time
    
    return arr #returns arr after deletions
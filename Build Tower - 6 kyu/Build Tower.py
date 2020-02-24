def tower_builder(n_floors):
    
    
    #first loop to fill tower
    tower = []
    cont = 0
    while (cont < n_floors):
        tower.append('*'+ 2*'*'*(cont))
        cont += 1
    
    #second loop to add blank spaces
    newt = []
    cont = 1
    for floor in tower:
        if(floor != tower[-1] ): #only add if not last floor
            newt.append(((len(tower)-cont)*' ') + (floor) + ((len(tower)-cont)*' '))
        cont += 1    
    newt.append(tower[-1]) #appending last floor
    return newt   

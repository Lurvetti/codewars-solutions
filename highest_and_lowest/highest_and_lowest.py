def high_and_low(numbers):
    n_array = numbers.split() #split string list
    n_int = [int(n) for n in n_array] #int transformation using list comprehention
    
    n_sorted = sorted(n_int) #sorting list
    
    return (str(n_sorted[-1]) + " " + str(n_sorted[0])) #returning

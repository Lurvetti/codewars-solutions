def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if((sq ** (1/2)).is_integer()): #testing if the result is an integer
        print("Number is a square: " + str((sq ** (1/2))))
        sq = sq + 1 #to start the loop right
        while(((sq ** (1/2)) % 1) != 0): #looping until net square
            sq = sq + 1
        return sq
    else:
        return -1

def dig_pow(n, p):
    sum = 0
    for digit in list(str(n)): #loop each char in the string made from the number n
        sum += pow(int(digit), p) #sum the powers
        p += 1 #iterate the powers
    if(sum % n == 0): #if sum can be divided by n, return the result = k
        return sum/n
    return -1    #if there is none, return -1

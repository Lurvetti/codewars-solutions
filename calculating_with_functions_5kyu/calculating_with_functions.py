#operations
def plus(sec, first = None): #will receive as parameters the second number for sure, and the first number on the second run
    print('\nPlus function')
    if (first != None): #test if there is a first number. If so, do the operation
        print('Result is: ' + str(first + sec))
        return (first + sec)
    else: #if not, return the operation type and the second number
        print('else')
        print(type(plus))
        return (plus,sec)

def minus(sec, first = None):
    print('\nMinus function')
    if (first != None):
        print('Result is: ' + str(first - sec))
        return (first - sec)
    else:
        print('else')
        print(type(plus))
        return (minus,sec)

def divided_by(sec, first = None):
    print('\nDivision function')
    if (first != None):
        print('Result is: ' + str(first/sec))
        return int((first/sec))
    else:
        print('else')
        print(type(plus))
        return (divided_by,sec)

def times(sec, first = None):
    print('\nTimes function')
    if (first != None):
        print('Result is: ' + str(first * sec))
        return (first * sec)
    else:
        print('else')
        print(type(plus))
        return (times,sec)

#numbers
def zero(op = None, sec = None, first = None): #receive operation informarion (function and second number)
    print('0 function')
    if (op!= None): #if there is info, unpack it
        operation, sec = op
    if(sec != None): #if I already have a second number, this is the first..so we call the operation again with the received number and this one
        return operation(sec, 0)
    else:
        return (0) # return this as second


def one(op = None, sec = None, first = None):
    print('1 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 1)
    else:
        return (1)
        
def two(op = None, sec = None, first = None):
    print('2 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 2)
    else:
        return (2)

def three(op = None, sec = None, first = None):
    print('3 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 3)
    else:
        return (3)

def four(op = None, sec = None, first = None):
    print('4 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 4)
    else:
        return (4)


def five(op = None, sec = None, first = None):
    print('5 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 5)
    else:
        return (5)

def six(op = None, sec = None, first = None):
    print('6 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 6)
    else:
        return (6)

def seven(op = None, sec = None, first = None):
    print('7 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 7)
    else:
        return (7)

def eight(op = None, sec = None, first = None):
    print('8 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        return operation(sec, 8)
    else:
        return (8)

def nine(op = None, sec = None, first = None):
    print('\n9 function')
    if (op!= None):
        operation, sec = op
    if(sec != None):
        print('if')
        return operation(sec, 9)
    else:
        print('else')
        return(9)

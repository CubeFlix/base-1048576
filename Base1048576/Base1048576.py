#!python3

# Base 1,048,576 Converter
# By Kevin Chen

# Note: When converting decimals, a character of unicode '\U00100004' will be added, to represent a decimal point, as it is out of the range of characters 1-1048576.
# Also, negitive signs will be represented by '\U00100005' and '\U00100006' will represent extra bits when encoding data.

# Copyright Kevin Chen 2020


import math

def splitnum(num): 
    return [char for char in num]

def convert(s): 
    new = "" 
  
    for x in s: 
        new += x  
  
    return new 


def ToBase1048576(num, **kwargs):

    MAX_DECIMAL_PLACES = 10

    if kwargs.get('maxDecimals') != None:
        MAX_DECIMAL_PLACES = kwargs.get('maxDecimals')
    
    if num < 0:
        sign = -1
    elif num == 0:
        return '\x00'
    else:
        sign = 1

    num *= sign

    digits = []
    decimalDigits = []
    hasDecimals = True
    try:
        splitnumbers = [int(str(num).split(".")[0]), float("0."+str(num).split(".")[1])]
    except:
        splitnumbers = [int(str(num).split(".")[0]), 0]
        hasDecimals = False
    splitnumbers.reverse()

    while splitnumbers[1]:
        n = splitnumbers[1] % 1048576
        digits.append(chr(int(n)))
        splitnumbers[1] = int(splitnumbers[1]/1048576)

    if sign < 0:
        digits.append('\U00100005')

    digits.reverse()
    
    if hasDecimals:
        lastNumber = splitnumbers[0]
        while lastNumber > 0 and len(decimalDigits) < MAX_DECIMAL_PLACES:
            decimalDigits.append(chr(int(str(lastNumber * 1048576).split('.')[0])))
            lastNumber = float("0."+str(lastNumber * 1048576).split('.')[1])
    
    
    if not hasDecimals:
        return convert(digits)
    else:
        return convert(digits + [chr(1048580)] + decimalDigits)


def FromBase1048576(unicodestring, **kwargs):
    chars = unicodestring.split('\U00100004')
    upperchars = splitnum(chars[0])
    hasDecimals = True
    try:
        lowerchars = splitnum(chars[1])
    except:
        hasDecimals = False
        

    digits = []
    lowerdigits = []

    
    if upperchars[0] == '\U00100005':
        upperchars.remove(upperchars[0])
        for upperchar in upperchars:
            digits.append(ord(upperchar))
        final = 0
        lowerfinal = 0
            
        digits.reverse()

        for num in digits:
            final += (num * pow(1048576, (digits.index(num))))

        if hasDecimals:
            for lowerchar in lowerchars:
                lowerdigits.append(ord(lowerchar))


            for lowernum in lowerdigits:
                final += (lowernum * pow(1048576, -(lowerdigits.index(lowernum)+1)))
                
        if kwargs.get("round") == True:
            return int(-final)
        else:
            return -final

                
    else:
        for upperchar in upperchars:
            digits.append(ord(upperchar))
        final = 0
        lowerfinal = 0
            
        digits.reverse()

        for num in digits:
            final += (num * pow(1048576, (digits.index(num))))

        if hasDecimals:
            for lowerchar in lowerchars:
                lowerdigits.append(ord(lowerchar))


            for lowernum in lowerdigits:
                final += (lowernum * pow(1048576, -(lowerdigits.index(lowernum)+1)))

        if kwargs.get("round") == True:
            return int(final)
        else:
            return final


def add(*argv):
    if(len(argv) < 2):
        raise TypeError("Insufficient Arguments")
    total = 0
    for arg in argv:
        total += FromBase1048576(arg)

    return ToBase1048576(total)

def sub(a, b):
    return ToBase1048576(FromBase1048576(a) - FromBase1048576(b))

def mul(*argv):
    if(len(argv) < 2):
        raise TypeError("Insufficient Arguments")
    total = 1
    for arg in argv:
        total *= FromBase1048576(arg)

    return ToBase1048576(total)

def div(a, b):
    return ToBase1048576(FromBase1048576(a) / FromBase1048576(b))
	

# Base 1,048,576 Converter
# By Kevin Chen

# Note: When converting decimals, a character of unicode '\U00100004' will be added, to represent a decimal point, as it is out of the range of characters 1-1048576.
# Also, negitive signs will be represented by '\U00100005'.

#todo: has no support for decimals or addng and subtracting, etc.

import math

MAX_DECIMAL_PLACES = 10

def splitnum(num): 
    return [char for char in num]

def convert(s): 
  
    new = "" 
  
    for x in s: 
        new += x  
  
    return new 


def ToBase1048576(num):
    
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


def FromBase1048576(unicodestring):
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
        for upperchar in range(1, len(upperchars)):
            digits.append(ord(upperchars[upperchar]))

        digits.reverse()

        for num in digits:
            
            final += (num * pow(1048576, (digits.index(num-1))))
        if hasDecimals:
            
            #lowerdigits.reverse()

            for lowerchar in range(1, len(lowerchars)):
                lowerdigits.append(ord(lowerchars[lowerchar]))


            for lowernum in lowerdigits:
                final += (num * pow(1048576, -(digits.index(num-1))))
                
        return -final

                
    else:
        for upperchar in range(0, len(upperchars)):
            digits.append(ord(upperchars[upperchar]))
        final = 0
        lowerfinal = 0
            
        digits.reverse()

        for num in digits:
            final += (num * pow(1048576, (digits.index(num))))

        if hasDecimals:
            #lowerdigits.reverse()
            
            for lowerchar in range(0, len(lowerchars)):
                lowerdigits.append(ord(lowerchars[lowerchar]))

            for lowernum in lowerdigits:
                lowerfinal += 1048576*lowernum
            lowerfinal = lowerfinal/pow(10, len(str(lowerfinal)))
            print(lowerfinal)
            
            return final + lowerfinal

	

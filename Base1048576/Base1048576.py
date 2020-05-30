# Base 1,048,576 Converter
# By Kevin Chen

# Note: When converting decimals, a character of unicode '\U00100004' will be added, to represent a decimal point, as it is out of the range of characters 1-1048576.

#todo: has no support for decimals

import math

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
        return 0
    else:
        sign = 1

    num *= sign

    digits = []
    decimalDigits = []


    splitnumbers = [int(str(num).split(".")[0]), int(str(num).split(".")[1])]
    splitnumbers.reverse()
    print(splitnumbers)

    while splitnumbers[1]:
        n = splitnumbers[1] % 1048576
        digits.append(chr(int(n)))
        
        splitnumbers[1] = int(splitnumbers[1]/1048576)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    decimalNums = splitnumbers[0]
    while decimalNums:
        n = decimalNums % 1048576
        decimalDigits.append(chr(int(n)))
        
        decimalNums = int(decimalNums/1048576)

    
    
    if splitnumbers[0] == 0:
        return convert(digits)
    else:
        return convert(digits + [chr(1048580)] + decimalDigits)


def FromBase1048576(unicodestring, posiitivity):
    chars = unicodestring.split('.')
    upperchars = splitnum(chars[0])
    lowerchars = splitnum(chars[1])

    digits = []
    lowerdigits = []

    
    if not posiitivity:
        for upperchar in range(1, len(upperchars)):
            digits.append(ord(upperchars[upperchar]))

        digits.reverse()

        for num in digits:
            final += (num * pow(1048576, (digits.index(num-1))))

        for lowerchar in range(1, len(lowerchars)):
            lowerdigits.append(ord(lowerchars[lowerchar]))

        lowerdigits.reverse()

        for lowernum in lowerdigits:
            final += (num * pow(1048576, -(digits.index(num-1))))
            
        return -final

    

                
    else:
        for char in range(0, len(chars)):
            digits.append(ord(chars[char]))

            final = 0
            
        digits.reverse()

        for num in digits:
            final += (num * pow(1048576, (digits.index(num))))
        return final

	

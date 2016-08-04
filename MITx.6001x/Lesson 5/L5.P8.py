#Lecture 5 Problem 8


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    aStr = aStr.lower()
    
    #Base case if string is empty
    if aStr == "":
        return False

    #Base  case if string is one character
    if len(aStr) == 1:
      return char == aStr
    
    #Base case if middle string character is the test case
    
    if char == aStr[len(aStr)/2]:
        return True    
    
    elif char > aStr[len(aStr)/2]:
       return isIn(char,aStr[len(aStr)/2+1:])
    
    elif char < aStr[len(aStr)/2]:
       return isIn(char,aStr[:len(aStr)/2] )           
#Problem Set 6 Problem 1
#CIPHER DICTIONARY

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """


    import string
    cipherDict = {}
    j = -26 + shift
    
    assert 0<= shift < 26, 'not between 0 and 25'

    for i in string.ascii_lowercase:
        cipherDict[i] = string.ascii_lowercase[j]
        j +=1

            
    
    #reset counter
    j = -26 + shift

     
    for i in string.ascii_uppercase:
        cipherDict[i] = string.ascii_uppercase[j]
        j +=1
        
                
    return cipherDict
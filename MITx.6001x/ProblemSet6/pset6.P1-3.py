#Problem Set 6 Problem 3

import string


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """



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
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newText = ''
    
    for i in text:
        if i in coder:
            newText += coder[i]
        else:
            newText += i
    
    return newText 
    
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    cipher = buildCoder(shift)
    return applyCoder(text,cipher)
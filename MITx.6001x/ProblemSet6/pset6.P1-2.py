#Problem Set 6 Problem 2
#apply the cipher

import string

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
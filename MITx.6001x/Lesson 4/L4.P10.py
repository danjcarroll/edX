#Lecture 4 Problem 10
#can't use in

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.upper()
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        izit = True
    else:
        izit = False
    return izit
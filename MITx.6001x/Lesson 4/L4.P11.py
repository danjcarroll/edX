#Lecture 4 Problem 11
# use in

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.upper()
    if char in 'AEIOU':
        izit = True
    else:
        izit = False
    return izit
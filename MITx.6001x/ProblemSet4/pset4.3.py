# Problem Set 4 Problem #3: Test word validity
#
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)



WORDLIST_FILENAME = "/Users/carrollfamily/Dropbox/code/MITx 6.00.1x/ProblemSet4/words.txt"

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        '''
        DJC: this assigns the frequency of a letter by looking up the
        frequency value in the dictionary and adding 1. If it's a new
        letter the default of 0 gets added to 1.
        At the same time it's defining or redefining the dictionary
        '''
        freq[x] = freq.get(x,0) + 1
    return freq


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def isValidWord(word, hand, wordList):

    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
   
#    numValid = 0
    isValid = True
    inList = False
    testDict = getFrequencyDict(word)
    
    if word == '':
        return False
    else:
        if word in wordList:
            inList = True

        for key in testDict:
            isValid = isValid and testDict[key] <= hand.get(key,-1)
        return inList and isValid
'''
            if testDict[key] <= hand.get(key,-1):
                numValid += testDict[key]
                print numValid
       
        if numValid == len(word):
            isValid = True
'''

    
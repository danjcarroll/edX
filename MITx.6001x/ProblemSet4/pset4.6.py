#Problem Set 4 Problem 6

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def getWordScore(word, n):
    wordScore = 0
    for alpha in word:
        wordScore += SCRABBLE_LETTER_VALUES[alpha]
    wordScore = wordScore * len(word)
    if len(word) == n:
        wordScore = wordScore + 50
    return wordScore

def isValidWord(word, hand, wordList):
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


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    tempScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    wordSoFar = None

    # For each word in the wordList
    for x in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(x, hand, wordList):
            # Find out how much making that word is worth
            tempScore = getWordScore(x, n)
            # If the score for that word is higher than your best score
            if tempScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = tempScore
                #print 'max score so far is: ', maxScore
                wordSoFar = x
                #print 'max word so far is: ', wordSoFar

    # return the best word you found.
    return wordSoFar
    
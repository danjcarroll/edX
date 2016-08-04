#Problem Set 3 Problem 2B

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    aStr = ''
  
    for alpha in secretWord:
        if alpha in lettersGuessed:
            aStr += alpha
        else:
            aStr += ' _ '

    return aStr
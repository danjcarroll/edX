def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = 'abcdefghijklmnopqrstuvwxyz'
    whats_left = ''
    
    for alpha in available:
        if alpha not in lettersGuessed:
            whats_left += alpha
    
    return whats_left
    
      
    
#Problem Set 3 Problem 2A

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    '''
    sw_list = []
 
    check_drop = lettersGuessed [:]


    for alpha in secretWord:
        sw_list.append(alpha)
  
    for alpha in secretWord:
        if alpha in check_drop:
            check_drop.remove(alpha)
            sw_list.remove(alpha)
                
    return len(sw_list) == 0
    
    '''
    alpha_test = len(secretWord)
    
    for alpha in secretWord:
        if alpha in lettersGuessed:
            alpha_test -= 1
            
    return alpha_test == 0
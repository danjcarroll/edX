#Problem Set 4 problem 4

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    valList = hand.values()
    handLen = 0
    
    for i in range(len(valList)):
        handLen += valList[i]
    
    return handLen
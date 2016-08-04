def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    big_length = 0

    #Base cases
    if len(aDict) == 0:
        return None
    
    if len(aDict) == 1:
        big_list = aDict.keys()
        return big_list[0]    
    
    for i in aDict:
        if len(aDict[i]) > big_length:
            big_length = len(aDict[i])
            big_key = i
        
    return big_key
    
 

    

        
    
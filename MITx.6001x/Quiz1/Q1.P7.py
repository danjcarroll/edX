#Quiz 1 Problem 7

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    
    result = []
    testDict = {}

    
    #aDict = {'adf':5,'zd':99,'c':0,'ddd':5,4:-88,'f':14}
    #aDict = {'a':5,'z':5,'c':5,'d':5,'e':5,'f':5}
    
    if len(aDict) == 0:
        return []
    
    if len(aDict) == 1:
        return aDict.keys()


    for key in aDict:
       
        testDict = aDict.copy()
        del testDict[key]
        
        if aDict[key] not in testDict.values():
            result.append(key)
                  
    result.sort()
    return result
    
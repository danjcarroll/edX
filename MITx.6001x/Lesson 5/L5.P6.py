#Lecture 5 Problem 6

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    aStr = aStr.lower()
    ans = 0
    for c in aStr:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans += 1
    return ans

#Lecture 6 Problem 7.A
testList = [1, -4, 8, -9]
'''
def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

def noNeg(a):
    return abs(a)
    
applyToEach(testList, noNeg)
'''
#Lecture 6 Problem 7.B
'''
def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

def AddOne(a):
    return a + 1
    
applyToEach(testList,AddOne)

'''
def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

def squareIt(a):
    return a**2
    
applyToEach(testList,squareIt)
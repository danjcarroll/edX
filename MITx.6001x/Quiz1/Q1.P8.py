#Quiz 1 Problem 8


def f(s):
    return 'a' in s

def satisfiesF(L):
    count = 0
    itList = L[:]
    
    for s in itList:
        if f(s) == True:
            count += 1
        else:
            L.remove(s)
    return count
    

run_satisfiesF(L,satisfiesF)
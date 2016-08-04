#Quiz 1 Problem 5

def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    result = []
    
    for i in range(2,N+1):
        notPrime = False
        for num in range(2,i):
            if i%num == 0:
                notPrime = True
        if notPrime == False:
            result.append(i)
    
    return result
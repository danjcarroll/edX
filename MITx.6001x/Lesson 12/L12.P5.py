#Lecture 12 Problem 5

def genPrimes():
    x = 2
    isItPrime = True
    primeList =[]

    while True:
        for p in primeList:         
            if (x % p) == 0:
                isItPrime = False
            
        if isItPrime == True:
            yield x
            primeList.append(x)
            x += 1
        else:
            #advance the count by one and reset the check
            x += 1
            isItPrime = True
            
"""
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
"""
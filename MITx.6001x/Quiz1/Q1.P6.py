#Quiz 1 Problem 6

def count7(N):
    '''
    N: a non-negative integer
    '''
    
    #these are the stopping conditions
    
    if N == 7:
        return 1
  
    elif N/10 == 0:
        return 0
   
    #recursion 
    
    elif N%10 == 7:
        return 1 + count7(N/10) 
    else:
        return 0 + count7(N/10)
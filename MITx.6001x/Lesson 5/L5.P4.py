def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''    
    
    if a > b:
        iter = b
    else:
        iter = a
    result = 1
    
    while result == 1 and iter > 1:
        if a % iter == 0 and b % iter == 0:
            result = iter
        else:
            iter -= 1
    return result
    
#######Course Answer

    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
        

#Lecture 7 Problem 7

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print x
    print a
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
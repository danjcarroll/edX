#Lecture 7 Problem 8

def f(n):
   """
   n: integer, n >= 0.
   """   
   while n > 1:
    return n * f(n-1)
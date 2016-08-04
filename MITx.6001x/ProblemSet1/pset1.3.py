#Problem Set 1 Problem 3

s = 'azcbobobegghaklbeghi'

def longest_alpha(s):
#    if s is None or len(s) <= 1:
#        return s

    longest = test = s[0]  #initialize variables

    for i in range(1, len(s)):  #start going through string
        if s[i] >= s[i - 1]:  #if letter is bigger alphabetically
            test += s[i]      #add it to the test string
        else:  #if current letter is not alpha> then 
            if len(longest) < len(test):  #test to see if it's longest so far
                longest = test  #reassign longest alphabetical string
            test = s[i]  #reset test case to one letter 'cuz you're starting over
#by using the following test you keep the first instance of the longest string
#because you're only going to replace it if it's bigger. Therefore you don't
#need to test which came first

    if len(longest) < len(test):
        longest = test
    return longest
    
print "Longest substring in alphabetical order is: ",longest_alpha(s)
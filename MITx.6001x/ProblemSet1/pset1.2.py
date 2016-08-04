#Problem Set 1 Problem 2

s = 'obooorobobobrobbobuobobowbobbobobfblob'

loc = 0
bob_count = 0

while loc <= len(s)-3:
    if s[loc] == 'b':
        if s[loc+1] == 'o':
                if s[loc+2] == 'b':
                    bob_count += 1
    loc += 1

print "Number of times 'bob' occurs: %d" %(bob_count)
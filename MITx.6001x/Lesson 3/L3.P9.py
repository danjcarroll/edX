#Lecture 3 Problem 9
guess = "h"
valid = True
high = 100
low = 0
izit = 0

print "Please think of a number between 0 and 100!"
	
izit = (high + low)/2

while guess != "c":
	print "Is your secret number %d?" % izit
	print "Enter 'h' to indicate the guess is too high. ",
	print "Enter 'l' to indicate the guess is too low. ",
	print "Enter 'c' to indicate I guessed correctly.",
	guess = raw_input("")
	
	if guess == 'c':
		break
	elif guess == 'h':
		high = izit
	elif guess == 'l':
		low = izit
	else:
		print "Sorry, I did not understand your input."
		
	izit = (high + low)/2

print "Game over. Your secret number was: %d" % izit	
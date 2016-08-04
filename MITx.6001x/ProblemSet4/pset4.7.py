#Problem Set 4 Problem 7

from ps4a import *
import time



def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    tempScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    wordSoFar = None

    # For each word in the wordList
    for x in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(x, hand, wordList):
            # Find out how much making that word is worth
            tempScore = getWordScore(x, n)
            # If the score for that word is higher than your best score
            if tempScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = tempScore
                #print 'max score so far is: ', maxScore
                wordSoFar = x
                #print 'max word so far is: ', wordSoFar

    # return the best word you found.
    return wordSoFar
  
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    # Keep track of the total score
    
    totalScore = 0
    
    # As long as there are still letters left in the hand:    
    while calculateHandlen(hand) > 0:
            
        # Display the hand
        print ('Current Hand: '),
        displayHand(hand)
        
        # Computer finds word
        word = compChooseWord(hand, wordList, n)
        
        # If the word is None type:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            totalScore += getWordScore(word, n)
            print ('"%s" earned %d points. Total: %d') % (word,getWordScore(word, n),totalScore)
            #print 
            # Update the hand
            hand = updateHand(hand, word)               

    # Game is over so tell user the total score

    print "Total score:", totalScore    

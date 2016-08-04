#Problem Set 2 Problem 2

#code grader variables
balance = 3926
annualInterestRate = 0.2



#program variables

paidOff = False
i = 1
minMonthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12.0
testBalance = balance

while paidOff == False:
  
    while i <= 12:
        unpaidBalance = testBalance - minMonthlyPayment
        testBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
        unpaidBalance = testBalance
        i += 1
        
    if testBalance <= 0:
            paidOff = True
    else:
        minMonthlyPayment += 10
        testBalance = balance
        i = 1
    

print "Lowest Payment: ", minMonthlyPayment
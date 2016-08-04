#Problem Set 2 Problem 3

#code grader variables
balance = 999999
annualInterestRate = 0.18

#program variables
low = balance / 12.0
high = balance *((1 + annualInterestRate)**12) / 12.0
epsilon = 0.01

paidOff = False
i = 1
minMonthlyPayment = (high + low)/2.0
monthlyInterestRate = annualInterestRate / 12.0
testBalance = balance


while abs(testBalance) >= epsilon:
    while i <= 12:
        testBalance = testBalance - minMonthlyPayment
        testBalance = testBalance * (1 + monthlyInterestRate)
        i += 1
        
    if testBalance > epsilon:
        low = minMonthlyPayment
        testBalance = balance
        
    elif testBalance < epsilon * -1:
        high = minMonthlyPayment
        testBalance = balance
    
    
    minMonthlyPayment = (high + low) / 2.0
    i = 1

print "Lowest Payment: %.2f" % minMonthlyPayment
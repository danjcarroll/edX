#Problem Set 2 Problem 1

#code grader variables
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


#program variables
totalPaid = 0.0
i = 1

monthlyInterestRate = annualInterestRate / 12.0

while i <=12:
    
    minMonthlyPayment = balance * monthlyPaymentRate
    
    unpaidBalance = balance - minMonthlyPayment

    balance = unpaidBalance + monthlyInterestRate * unpaidBalance
    
    balance = round(balance,2)
    minMonthlyPayment = round(minMonthlyPayment,2)
    
    totalPaid = totalPaid + minMonthlyPayment
    
    print "Month: ", i
    print "Minimum monthly payment: %.2f" % minMonthlyPayment
    print "Remaining balance: %.2f" % balance
    
    i += 1
    
print "Total paid: %.2f" % totalPaid
print "Remaining balance: %.2f" % balance
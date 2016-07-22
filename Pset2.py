"""
required math: 
monthly interest rate = annual interest rate/12
minimum monthly payment = min monthly payment rate X previous balance
monthly unpaid balance = previous balance - min monthly payment 
updated balance each month = monthly unpaid balance + (monthly interest rate X monthly unpaid balance)
NEED TO PRINT: 
Month: 
Minimum monthly payment: 
Remaining balance: 
"""
#don't specify variables balance, annualInterestRate, monthlyPaymentRate
#balance = 4213
#annualInterestRate = .2
#monthlyPaymentRate = .04
#total_paid = 0

def question1():
	for month in range(1,13):
		monthly_interest_rate = annualInterestRate/12
		min_monthly_payment = monthlyPaymentRate*balance
		monthly_unpaid_balance = balance - min_monthly_payment
		balance = monthly_unpaid_balance + (monthly_interest_rate*monthly_unpaid_balance)
		total_paid += min_monthly_payment
		print "Month:" + str(month) 
		print "Minimum monthly payment:" + str(round(min_monthly_payment,2))
		print "Remaining balance:" + str(round(balance,2))
		if month == 12:
			print "Total paid:" + str(round(total_paid,2))
			print "Remaining balance:" + str(round(balance,2))



#balance = 4773 
#annualInterestRate = .2 
#updatedBalance = balance 
def question2():
	lowestPayment = 10
	monthlyInterestRate = annualInterestRate/12
	while updatedBalance > 0:
		for month in range(1,13):
			monthlyUnpaidBalance = updatedBalance - lowestPayment
			updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
		if updatedBalance < 0: 
			print "Lowest Payment:" + str(lowestPayment)
		else: 
			updatedBalance = balance
			lowestPayment+=10

def question3():
	updatedBalance = balance
	monthlyInterestRate = annualInterestRate/12
	paymentLb = balance/12
	paymentUb = (balance*(1+monthlyInterestRate)**12)/12
	mid = (paymentLb + paymentUb)/2
	while (updatedBalance > .01) or (updatedBalance < -.01):
		for month in range(1,13):
			monthlyUnpaidBalance = updatedBalance - mid
			updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
		if updatedBalance > .01: 
			paymentLb = mid
			mid = (paymentUb+paymentLb)/2
			updatedBalance = balance
		elif updatedBalance < -.01:
			paymentUb = mid 
			mid = (paymentUb+paymentLb)/2
			updatedBalance = balance
		else: 
			mid = round(mid,2)
			print "lowestPayment:" + str(mid)

	





# Get details for loan
money_owed = float(input('How much money do you owe in INR?\n')) # 25,000
apr = float(input("What is the annual interest rate for the loan?\n")) # 2.1 annual percentage rate of interest
payment_per_month = float(input('How much amount will you pay for a month?\n')) # 2,000
# emi_duration = int(input('How many months do you want to see the results?\n')) # 24

monthly_rate = apr / 100 / 12

is_loan_paid = False
installment_month = 0

while (is_loan_paid == False and installment_month >= 0):

    # Calculate the interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in the interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment_per_month < 0):
        print('The last payment is, ', money_owed)
        print(f'You paid off the loan in {installment_month + 1} months')
        is_loan_paid = True
        break

    # Make payment
    money_owed = money_owed - payment_per_month

    print('Paid', payment_per_month, f"for the {installment_month + 1} month", 'of which', interest_paid, 'was interest,', end=" ")
    print('Now I owe', money_owed)

    installment_month = installment_month + 1

# count = 0
# while (is_loan_paid == False and installment_month >= 0):
#     print('Inside the loop')
#     count += 1 
#     is_loan_paid = True
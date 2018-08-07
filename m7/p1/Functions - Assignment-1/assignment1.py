"""
A program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required
by the credit card company each month.
"""
def credit_payment(balance, annual_interestrate, monthly_paymentrate):
    """ Function to calculate balance after an year"""
    outstanding_balance = balance
    def monthly_payment(credit_amount):
        return credit_amount*monthly_paymentrate

    def bal_mon(credit_amount):
        return credit_amount + credit_amount*(annual_interestrate/12)

    i = 1
    balance_due = outstanding_balance
    while i <= 12:
        payment = monthly_payment(balance_due)
        unpaid_balance = balance_due - payment
        balance_due = bal_mon(unpaid_balance)
        # print(round(balance_due, 2))
        i += 1
    return round(balance_due, 2)
def main():
    """
    Function to check test cases
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: " + str(credit_payment(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()

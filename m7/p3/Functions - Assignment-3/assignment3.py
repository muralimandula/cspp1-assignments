"""
A program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months
using bi-section method
"""

def payingdebt_offinayear(balance, annual_interestrate):
    """    A function to calculate the lowest payment"""
    def bal_d(balance, pay, annual_interestrate):
        """ A function to calculate balance"""
        balnace_due = balance
        for _ in range(1, 13):
            unpaid_balance = balnace_due - pay
            balnace_due = unpaid_balance*(1 + (annual_interestrate/12.0))
        return balnace_due

    payment_low = balance/12.0
    monthly_interestrate = annual_interestrate/12.0
    payment_high = (balance*((1 + monthly_interestrate)**12))/12.0
    payment = (payment_high + payment_low)/2.0
    epsilon = 0.05556

    while True:
        # print(bal_d(balance, payment, annual_interestrate))
        if  bal_d(balance, payment, annual_interestrate) > epsilon:
            payment_low = payment
        elif bal_d(balance, payment, annual_interestrate) < -epsilon:
            payment_high = payment
        else:
            return round(payment, 2)
        payment = (payment_high + payment_low)/2.0
    # if bal_d(balance, payment, annual_interestrate) <= epsilon:

def main():
    """
    A function for output
    """
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(payingdebt_offinayear(data[0], data[1])))
if __name__ == "__main__":
    main()

"""
A program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months
"""

def payingdebtoff_inayear(balance, annual_interestrate):
    """
    A function to calculate the lowest payment
    """
    payment = 0
    bal_due = balance
    while bal_due > 0:
        payment += 10
        bal_due = balance
        for _ in range(1, 13):
            unpaid_bal = bal_due - payment
            bal_due = unpaid_bal*(1 + (annual_interestrate/12.0))
    return payment

def main():
    """
    Function to check test cases
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+ str(payingdebtoff_inayear(data[0], data[1])))

if __name__ == "__main__":
    main()

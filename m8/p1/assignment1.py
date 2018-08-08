"""# Exercise: Assignment-1
# Write a Python function, factorial(n),
that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number."""
def factorial(input_num):
    '''n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if input_num <= 1:
        return 1
    return input_num*factorial(input_num-1)

def main():
    """Main Function"""
    input_num = input()
    print(factorial(int(input_num)))
main()

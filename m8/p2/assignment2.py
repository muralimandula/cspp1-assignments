"""# Exercise: Assignment-2
# Write a Python function, sumofdigits,
that takes in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number."""
def sumofdigits(input_number):
    '''n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if  input_number == 0:
        return 0
    return input_number%10 + sumofdigits(input_number//10)

def main():
    """Main Function"""
    input_number = input()
    print(sumofdigits(int(input_number)))

main()

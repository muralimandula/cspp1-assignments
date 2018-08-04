'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
PRODUCT = 1
NUM = int(input())
while NUM >= 1:
    REM = NUM%10
    PRODUCT = PRODUCT * REM
    NUM = NUM/10
print(PRODUCT)

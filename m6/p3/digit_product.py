'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''

NUM = int(input())
PRODUCT = 1
REM = 0
X = 1
if NUM < 0:
    X = -1
    NUM = abs(NUM)
else:
	X = 1
if NUM != 0:
    while NUM >= 1:
        REM = NUM%10
        PRODUCT = int(PRODUCT) * int(REM)
        NUM = NUM//10
    print(PRODUCT*X)
else:
    print("0")

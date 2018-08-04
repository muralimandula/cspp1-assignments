'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
PRODUCT = 1
NUM = int(input())
TEMP = 0
if NUM == 0:
    print(NUM)

elif NUM < 0:
    NUM = -NUM
    TEMP = 1
while NUM >= 1:
    REM = NUM%10
    PRODUCT = PRODUCT * int(REM)
    NUM = NUM/10
if TEMP == 1:
    print(-PRODUCT)
elif NUM != 0:
    print(PRODUCT)

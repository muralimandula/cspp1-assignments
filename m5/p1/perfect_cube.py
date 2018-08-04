""" Write a python program to find if the given number is a perfect cube or not"""
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

CUBE = int(input())
GUESS = 1
while (GUESS**3) < CUBE:
    GUESS += 1
if int(GUESS**3) == CUBE:
    print(CUBE, "is a perfect cube")
else:
    print(CUBE, "is not a perfect cube")

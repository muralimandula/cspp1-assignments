"""# Write a python program to find the square root of the given number"""
# using Newton raphson method
EPSILON = 0.01
X_NUM = int(input())
GUESS_VAL = X_NUM/2.0
while abs(GUESS_VAL*GUESS_VAL - X_NUM) >= EPSILON:
    GUESS_VAL = GUESS_VAL - (((GUESS_VAL**2) - X_NUM)/(2*GUESS_VAL))
print(str(GUESS_VAL))

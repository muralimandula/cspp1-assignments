"""# Write a python program to find the square root of the given number"""
# using approximation method
# your code starts here

X_NUM = int(input())
EPSILON = 0.01
LOWER = 0.0
HIGHER = X_NUM
BI_VAL = (HIGHER + LOWER)/2.0
while abs(BI_VAL**2 - X_NUM) > EPSILON:
    if BI_VAL**2 < X_NUM:
        LOWER = BI_VAL
    else:
        HIGHER = BI_VAL
    BI_VAL = (HIGHER + LOWER)/2.0
print(BI_VAL)

"""Assume s is a string of lower case characters."""
STR_A = input()
SUB_A = 'bob'
C_OUNT = 0
for i in range(len(STR_A)):
    if SUB_A == STR_A[i:i+3]:
        C_OUNT += 1
print(C_OUNT)

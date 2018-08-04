"""Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
# the input string is in s
# remove pass and start your code here"""
STR_A = input()
SUB_A = 'bob'
C_OUNT = 0
for i in range(len(STR_A)):
    if SUB_A == STR_A[i:i+3]:
        C_OUNT += 1
print(C_OUNT)

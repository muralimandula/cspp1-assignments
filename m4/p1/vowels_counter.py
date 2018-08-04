"""#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5"""
S_S = input()
# the input string is in s
# remove pass and start your code here
C_OUNT = 0
for X in S_S:
    if X in "aeiouAEIOU":
        C_OUNT += 1
print(C_OUNT)

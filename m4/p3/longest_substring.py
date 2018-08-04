"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s,
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head."""
STR_S = input()
LONG_END_POS = 0
LONG_COUNT = 0
CHAR_COUNT = 0
for i in range(len(STR_S)-1):
    if STR_S[i] <= STR_S[i+1]:
        CHAR_COUNT += 1
    else:
        CHAR_COUNT = 0
    if  CHAR_COUNT > LONG_COUNT:
        LONG_COUNT = CHAR_COUNT
        LONG_END_POS = i
        LONG_START = LONG_END_POS-LONG_COUNT+1
print(STR_S[LONG_START:LONG_START+LONG_COUNT+1])

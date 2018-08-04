'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
STR = input()
NEW_STR = ""
C_OUNT = 0
for X in STR:
    if X in "!@#$%^&*":
        NEW_STR = NEW_STR+" "
    else:
        NEW_STR = NEW_STR+X
print(NEW_STR)

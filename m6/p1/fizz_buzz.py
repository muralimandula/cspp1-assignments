'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''


NUMBER = int(input())
I = 1
while I <= NUMBER:
    if (I%3 == 0) and (I%5 == 0):
        print("Fizz")
        print("Buzz")
    elif I%3 == 0:
        print("Fizz")
    elif I%5 == 0:
        print("Buzz")
    else:
        print(I)
    I += 1

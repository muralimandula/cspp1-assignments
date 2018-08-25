'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """main function"""
    no_of_lines = int(input())
    for _ in range(no_of_lines):
        string = ""
        string += input()
        print(string)


if __name__ == '__main__':
    main()

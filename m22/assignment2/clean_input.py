'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re

def clean_string(string):
    """cleaning the input"""
    cleanup = re.compile('[^a-zA-Z0-9]')
    string = cleanup.sub('', string)
    return string

def main():
    """Main function"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

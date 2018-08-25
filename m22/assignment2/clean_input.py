'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

    # regex = re.compile('[^a-z]')                          # cap-'^' mean only, i.e., only a to z
    # # print([regex.sub('', word.strip()) for word in input_value.lower().split(' ')])
    # return [regex.sub('', word.strip()) for word in input_value.lower().split(' ')]

import re

def clean_string(string):
    """cleaning the input"""
    cleanup = re.compile('[^a-z A-Z 0-9]')
    string = cleanup.string
    return string

def main():
    """Main function"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

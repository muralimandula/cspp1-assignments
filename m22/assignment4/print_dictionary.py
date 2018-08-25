'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    """printing dictionary"""
    for each_key in sorted(dictionary.keys()):
        print(each_key, "-", dictionary[each_key])

def main():
    """Main function"""
    dictionary = eval(raw_input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()

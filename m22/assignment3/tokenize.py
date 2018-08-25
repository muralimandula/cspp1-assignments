'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(input_list):
    """tokenize or word frequency"""
    input_dict = {}
    for each_word in set(input_list):
        input_dict[each_word] = input_list.count(each_word)

    return input_dict

            
def main():
    """Main FUnction"""
    no_of_lines = int(input())
    input_list = []
    for _ in range(no_of_lines):
        input_list = input().split()   # list of lists

    print(tokenize(input_list))

if __name__ == '__main__':
    main()

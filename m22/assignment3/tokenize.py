'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(input_list):
    """tokenize or word frequency"""
    input_dict = {}
    # for each_word in set(input_list):
    #     input_dict[each_word] = input_list.count(each_word)

    for each_word in input_list:
        if each_word not in input_dict:
            input_dict[each_word] = 1
        else:
            input_dict[each_word] += 1

    return input_dict

def clean_string(input_list):
    """cleaning the input"""
    cleanup = re.compile('[^a-zA-Z ]')
    input_list = [cleanup.sub('', word) for word in input_list]
    return input_list
            
def main():
    """Main FUnction"""
    no_of_lines = int(input())
    input_list = []
    if no_of_lines = 1:
        for _ in range(no_of_lines):
            input_list = input().split()   # list
    else:
        for _ in range(no_of_lines):
            input_list.append(input().split())  # list of lists
        input_list = input_list[0] + input_list[1]

    print(tokenize(clean_string(input_list)))

if __name__ == '__main__':
    main()

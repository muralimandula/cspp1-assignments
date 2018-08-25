'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """frequency calculator"""
    for each_key in sorted(dictionary.keys()):
        # print(each_key, "-", (string "#" for _ in range(dictionary[each_key])))
        string = ''
        for _ in range(dictionary[each_key]):
            string += '#'
        print(each_key, "-", string)


def main():
    """Main Function"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()

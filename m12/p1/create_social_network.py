"""
'''
    Assignment-1 Create Social Network
'''


#def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
#    return data"""

def main():
    '''
        handling testcase input and printing output
    '''
    input_lines = input()
    adict = {}
    for _ in range(int(input_lines)):
        data = input()
        if 'follows' in data:
            list_value = data.split(" follows ")
            if list_value[0] not in adict:
                adict[list_value[0]] = list_value[1].split(',')
            else:
    #          adict[list_value[0]] = list_value[1].append(list_value[1].split(','))
                adict[list_value[0]].extend(list_value[1].split(','))
        # print(create_social_network(adict))
        else:
            break
    print(adict)

if __name__ == "__main__":
    main()

'''
    Document Distance - A detailed description is given in the PDF
'''


def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    main_dict = {}
    list1 = dict1.split()
    list2 = dict2.split()
    list_main = set(list1+list2)
    for word in list_main:
    	count = 0
    	for i in range(len(list1)):
    	    if word == list1[i]:
    	    	count += 1

    	main_dict[word] = count
    	count = 0
    	for i in range(len(list2)):
    	    if word == list2[i]:
    	    	count += 1
    	main_dict[word].append(count)

    print(main_dict)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

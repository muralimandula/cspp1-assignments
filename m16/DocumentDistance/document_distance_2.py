'''
   Document Distance - A detailed description is given in the PDF
'''
import re
import math

def clean(input_value):
    '''
        Make a words list and clean up the words, eliminating all special characters and numbers
    '''
    regex = re.compile('[^a-z]')                          # cap-'^' mean only, i.e., only a to z
    # print([regex.sub('', word.strip()) for word in input_value.lower().split(' ')])
    return [regex.sub('', word.strip()) for word in input_value.lower().split(' ')]

def word_frequency(list_of_words, index, dictionary):
    stop_words = load_stopwords('stopwords.txt')             # loading words from the .txt file
    for word in list_of_words:
        if word != "" and word not in stop_words:
            if word not in dictionary:
                dictionary[word] = [0, 0]
            dictionary[word][index] += 1
    return dictionary

def computation(dictionary):
    num = sum(value[0]*value[1] for value in dictionary.values())
    den1 = math.sqrt(sum(value[0]**2 for value in dictionary.values()))
    den2 = math.sqrt(sum(value[1]**2 for value in dictionary.values()))
    return num/(den1*den2)


def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    input1_list = clean(input1)
    input2_list = clean(input2)

    dictionary = {}
    dictionary = word_frequency(input1_list, 0, {})
    dictionary = word_frequency(input2_list, 1, dictionary)

    return computation(dictionary)

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
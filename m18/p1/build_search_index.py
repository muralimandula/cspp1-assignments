'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

def build_search_index(cleaned_documents_list):
    '''
        Process the cleaned_document_list step by step as given below
    '''
    search_engine_words = {}
    stop_words = load_stopwords('stopwords.txt')
    main_list = []
    re_main_list = []
    for i in range(len(cleaned_documents_list)-1):
        main_list += cleaned_documents_list[i] + cleaned_documents_list[i+1]
    # main_list = set(main_list)                                                # unique words
    for word in main_list:
        if word not in stop_words:
            re_main_list.append(word)
    # print(main_list)

    for word in set(re_main_list):   # main list is the list of cleaned,unique words in lower case
        count0 = cleaned_documents_list[0].count(word)
        count1 = cleaned_documents_list[1].count(word)
        count2 = cleaned_documents_list[2].count(word)
        count3 = cleaned_documents_list[3].count(word)
        count4 = cleaned_documents_list[4].count(word)
        count5 = cleaned_documents_list[5].count(word)
        search_engine_words[word] = [(0, count0), (1, count1), (2, count2), (3, count3), (4, count4), (5, count5)]

    return search_engine_words


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(search_index):
    '''
        print the search search_index
    '''
    # for word in search_index:
    #     print(search_index)
    #     for i in range(6):
    #         if search_index[word][i][1] == 0:
    #             del(search_index[word][i])

    keys = sorted(search_index.keys())
    # print(sorted(search_index))
    for key in keys:
        print(key, " - ", keys[key])


    # for key in search_index:
    #     while (0,0) in search_index[key]:
    #         search_index

def word_list(documents_list):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the document by remvoing all the non alphabet characters
        return a list of words
    '''
    regex = re.compile('[^a-z]')              # cap-'^' mean only, i.e., only a to z
    for i in range(len(documents_list)):
        for _ in range(len(documents_list[i])):
            documents_list[i] = [regex.sub('', word.lower().strip()) for word in documents_list[i]]
    return documents_list

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents_list = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents_list to the list
    for i in range(lines):
        input_document = input()
        documents_list.append(input_document.split())
        i += 1

    # call print to display the search index
    # print(documents_list)
    print_search_index(build_search_index(word_list(documents_list)))

if __name__ == '__main__':
    main()

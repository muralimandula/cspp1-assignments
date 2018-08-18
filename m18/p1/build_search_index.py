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

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    search_index = {}                                           
    search_index = tokenize(docs, 0, {})
    search_index = tokenize(docs, 1, search_index)
    search_index = tokenize(docs, 2, search_index)
    search_index = tokenize(docs, 3, search_index)
    search_index = tokenize(docs, 4, search_index)
    search_index = tokenize(docs, 5, search_index)


    return search_index    


def tokenize(list_of_words_in_docs, index, search_engine_words):
    """
    calculating the frequency
    """
    stop_words = load_stopwords('stopwords.txt')             # loading words from the .txt file
    
    for word in list_of_words_in_docs:
        if word != "" and word not in stop_words:            # only, if not a stop word
            if word not in search_engine_words:                    # adding non stop words into search engine
                search_engine_words[word] = [0, 0]                       #### when not exist
            search_engine_words[word][index] += 1                        #### when already exists
    
    return search_engine_words                                     # return search engine of non stop words (Dictionary)



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
    keys = sorted(search_index.keys())
    for key in keys:
        print(key, " - ", search_index[key])


def word_list(document):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the document by remvoing all the non alphabet characters
        return a list of words
    '''
    regex = re.compile('[^a-z]')               # cap-'^' mean only, i.e., only a to z
    return [regex.sub('', word.strip()) for word in document[0].lower().split(' ')]  


# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input().split())
        i += 1

    # call print to display the search index
    print(documents)
    print_search_index(build_search_index(word_list(documents)))

if __name__ == '__main__':
    main()
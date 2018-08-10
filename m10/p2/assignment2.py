'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # WORDSLIST: list of strings
    w_list = line.split()
    print("  ", len(w_list), "words loaded.")
    return w_list

def choose_word(wrd_lst):
    """
    wrd_lst (list): list of words (strings)

    Returns a word from wrd_lst at random
    """
    return random.choice(wrd_lst)

# end of helper code
# -----------------------------------

# Load the list of words into the variable WORDSLIST
# so that it can be accessed from anywhere in the program
WORDSLIST = load_words()

def hangman(secret_word_input):
    '''
    secret_word_input: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word_input contains.
    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word_input), "letters long.")
    guessed_letter = ''
    store_string = ''
    store_string = store_string + guessed_letter
    for num_guess in range(len(secret_word_input)+3, 0, -1):
        if get_guessed_word(secret_word_input, store_string) != secret_word_input:
            print('You have', num_guess, 'guesses left')
            print('Available Letters: ', get_available_letters(store_string))
            guessed_letter = input('Please guess a letter: ')
            store_string += guessed_letter
            if is_word_guessed(secret_word_input, guessed_letter):
                print("Good guess: ", get_guessed_word(secret_word_input, store_string))
            else:
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word_input, store_string))
        else:
            return print("Congratulations!")
    return print("Sorry you've run out of guesses. The word was", secret_word_input)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    compare_string = ['_']*len(secret_word)
    for [i, _] in enumerate(letters_guessed):
        for [j, _] in enumerate(secret_word):
            if letters_guessed[i] == secret_word[j]:
                compare_string[j] = secret_word[j]

    compare_string = ''.join(compare_string)
    return compare_string

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #compare_string = ['']*len(secret_word)
    #for [i, _] in enumerate(letters_guessed):
    for [j, _] in enumerate(secret_word):
        if letters_guessed == secret_word[j]:
            return True
    return False

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #compare_string = 'abcdefghijklmnopqrstuvwxyz'
    import string
    compare_string = string.ascii_lowercase
    for ch_ar in letters_guessed:
        if ch_ar in compare_string:
            compare_string = compare_string.replace(ch_ar, '')
    return compare_string

def main():
    '''
    Main function for the given program

    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    sec_word = choose_word(WORDSLIST).lower()
    hangman(sec_word)
    #hangman("apple")

if __name__ == "__main__":
    main()

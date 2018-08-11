"""#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has no side effects:
i.e., it must not mutate the hand passed in. Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py."""


def updateHand(hand_dictionary, word_data):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for char in word_data:
        if char in hand_dictionary:
            hand_dictionary[char] = hand_dictionary[char]-1
    print(hand_dictionary)

def main():
    length_of_list = input()
    hand_dictionary = {}
    for i in range(int(length_of_list)):
        data = input()
        list_in_hand = data.split()
        hand_dictionary[list_in_hand[0]] = int(list_in_hand[1])
    word_data = input()
    updateHand(hand_dictionary,word_data)
        


if __name__== "__main__":
    main()
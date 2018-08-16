'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    """'''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    praveen 2 is below'''
        # if A in join()
    praven1 is below
    hand_cards = []
    for c, s in hand:
        hand_cards.append(c)

    card_value = '--23456789TJQKA'

    hand_cards_values = []

    for a_card in hand_cards:
        hand_cards_values.append(card_value.index(a_card))

    hand_cards_values
"""
    card_value_praveen = set('--23456789TJQKA'.index(c) for c, s in hand)
    short = card_value_praveen
    # card_value_praveen = set(card_value_praveen)
    return len(short) == len(hand) and (max(short)-min(short) == 4)

def is_flush(hand):
    '''
    How do we find out if the given hand is a flush?
    The hand has a list of cards represented as strings.
    Do we need both the characters in the string? No.
    The second character is good enough to determine a flush
    Think of an algorithm: given the card suite how to check if it is a flush
    Write the code for it and return True if it is a flush else return False
        """ I did
    for i in range(len(hand)-1):
        if hand[i][1] != hand[i+1][0]
            return False
    return True
    """
    '''
    suit_set = set()
    for each_card in hand:
        suit_set.add(each_card[1])

    return len(suit_set) == 1

def of_a_kind(hand):
    """ of a kind for hand """
    # max_kind = 1
    pair_hand = []
    counted = []
    card_value_kind = ['--23456789TJQKA'.index(c) for c, s in hand]
    length = len(card_value_kind)
    # print("\n", card_value_kind)
    for i in range(length):
        hand_kind_count = 0
        if card_value_kind[i] not in counted:
            for j in range(length):
                if card_value_kind[i] == card_value_kind[j]:
                    hand_kind_count += 1

            # if hand_kind_count >= max_kind:
            #     max_kind = hand_kind_count
            pair_hand.append(hand_kind_count)
            # pair_hand.append(hand_kind_count)
            counted.append(card_value_kind[i])
    # print("\n")
    # print(hand, "76")
    # print(pair_hand)

    if 5 in pair_hand:                       #0 five of a kind
        # print("five of a kind")
        return_value = 0

    flush = is_flush(hand)
    straight = is_straight(hand)
    if flush and straight is True:           #1 straight flush
        # print(" straight flush")
        return_value = 1

    if 4 in pair_hand:                       #2 four of a kind
        # print("four of a kind")
        return_value = 2
    if 3 in pair_hand and 2 in pair_hand:    #3 full house
        # print("full house")
        return_value = 3

    if flush is True:                        #4 flush
        # print("flush")
        return_value = 4

    if straight is True:                     #5 straight
        # print("Straight")
        return_value = 5

    if 3 in pair_hand and 1 in pair_hand:    #6 three of a kind
        # print("three of a kind")
        return_value = 6
    if pair_hand.count(2) == 2:              #7 two pairs
        # print("two pairs")
        return_value = 7
    if 2 in pair_hand and pair_hand.count(1) == 3:  #8 only one pair
        # print("one pair of a kind")
        return_value = 8

    # print("High card")                       #9 High card
    return_value = 9

    return return_value




def hand_rank(hand):
    """
    You will code this function. The goal of the function is to
    return a value that max can use to identify the best hand.
    As this function is complex we will progressively develop it.
    The first version should identify if the given hand is a straight
    or a flush or a straight flush.
    """

    # flush = is_flush(hand)
    # straight = is_straight(hand)
    a_kind = of_a_kind(hand)
    # if flush and straight is True:
    #     return 1
    # if flush is True:
    #     return 4
    # if straight is True:
    #     return 5
    return a_kind

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example King of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
def poker(hands):
    '''
    This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return min(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))

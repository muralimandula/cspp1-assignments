'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
deck = {'diamond_red': ['2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD'],
'heart_red' : ['2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH'],
'club_black': ['2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC'],
'spade_black' : ['2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS']}

def int_cast(card_value):
    if card_value[0] == 'T':
        return 10
    elif card_value[0] == 'J':
        return 11
    elif card_value[0] == 'Q':
        return 12
    elif card_value[0] == 'K':
        return 13
    elif card_value[0] == 'A':
        return 14
    return int(card_value)


def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    hand = sorted(hand, key=int_cast)
    print(hand)
    straight_count = 0
    for i in range(len(hand)-1):
        if int_cast(hand[i][0])+1 == int_cast(hand[i+1][0]):
            straight_count += 1
    print(straight_count)
    if straight_count == len(hand)-1:
        return True
    False



def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    
    for suite in deck:
        flush_count = 0
        for card_value in hand:
            if card_value in deck[suite]:
                flush_count +=1
    print(flush_count)
    if flush_count == len(hand)-1:
        return True
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    flush = is_flush(hand)
    straight = is_straight(hand)
    if flush and straight == True:
        return 3

    elif flush == True:
        return 2

    elif straight == True:
        return 1
    return 0

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
    # print(hands)
    
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)  #will return only one max list

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

'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
# import collections

def crd_v(hand):
    '''calculates card values'''
    excep = [2, 3, 4, 5, 14]
    crd_val = ['--23456789TJQKA'.index(c) for c, s in hand]
    if crd_val == excep:
        crd_val.remove(14)
        crd_val.add(1)
    crd_val = sorted(crd_val, reverse=True)
    return crd_val

def is_straight(hand):
    ''' Straight hand function '''
    return len(crd_v(hand)) == 5 and (max(crd_v(hand))-min(crd_v(hand)) == 4)

def is_flush(hand):
    ''' flush hand function '''
    return len(set(s for c, s in hand)) == 1

def kind(hand, n_len):
    ''' To determine the kind of the function'''
    for ranks in crd_v(hand):
        if crd_v(hand).count(ranks) == n_len:
            return ranks
    return None

# def is_four_of_a_kind(hand):
#     ''' Four of a kind hand function '''
#     return list(collections.Counter(crd_v(hand)).values()) == [4, 1]

# def is_fullhouse(hand):
#     ''' Full House hand function '''
#     return sorted(list(collections.Counter(crd_v(hand)).values())) == [2, 3]

# def is_three_of_kind(hand):
#     ''' Three of kind hand function '''
#     bool_val = sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 1, 3]
#     return bool_val

# def is_twopair(hand):
#     ''' Two pair hand function '''
#     bool_val = sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 2, 2]
#     return bool_val

# def is_onepair(hand):
#     ''' One pair hand function '''
#     bool_val = sorted(list(collections.Counter(crd_v(hand)).values())) == [1, 1, 1, 2]
#     return bool_val

def hand_rank(hand):
    ''' ranks the card '''
    hand_ranks = crd_v(hand)
    rank = (0, hand_ranks)
    if is_flush(hand) and is_straight(hand):
        rank = (8,)
    # four of a kind
    elif kind(hand, 4):
        rank = (7,)
    # full house
    elif kind(hand, 3) and kind(hand, 2):
        rank = (6, )
    elif is_flush(hand):
        rank = (5, hand_ranks)
    elif is_straight(hand):
        rank = (4, hand_ranks)
    # three of a kind
    elif kind(hand, 3):
        return (3, kind(hand, 2), hand_ranks)
    # Two pair
    elif kind(hand, 2) and kind(sorted(hand, reverse=True), 2) and kind(\
    hand, 2) != kind(sorted(hand, reverse=True), 2):
        return (2, kind(hand, 2), kind(sorted(hand, reverse=True), 2))
    # one pair
    elif kind(hand, 2):
        return (1, kind(hand, 2))
    return rank

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)

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

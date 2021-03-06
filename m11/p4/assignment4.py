"""#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code."""


def hand_value(hand_list):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_val = 0
    for key_dict in hand_list:
        sum_val += hand_list[key_dict]
    return sum_val

def main():
    """MainmFUnction"""
    input_num = input()
    adict = {}
    for _ in range(int(input_num)):
        data = input()
        list_value = data.split()
        adict[list_value[0]] = int(list_value[1])
    print(hand_value(adict))


if __name__ == "__main__":
    main()

'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''

def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    # remove the pass below and start writing your code
    if arg1 in network:
        print(arg1)
        print(arg2)
        network[arg1].append(arg2)
    return network

def unfollow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    # remove the pass below and start writing your code
 #   if arg1 in network:
  #      del network[arg1].values(arg2)
    if arg1 in network and arg2 in network[arg1]:
        network[arg1].remove(arg2)
    return network
def delete_person(network, arg1):
    '''
        2 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 is a person in the network
        delete_person function is called when arg1 wants to exit from the network
        so, this should result in deleting arg1 from network
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the network dictionary and return it
    '''
    # remove the pass below and start writing your code
    print(type(network))
    if arg1 in network:
        del network[arg1]
    for key in network:
        if arg1 in network[key]:
            network[key].remove(arg1)
    return network
def main():
    '''
        handling testcase input and printing command
    '''
    network = input()
    network1 = {}
    no_of_commands = int(input())
    for _ in range(int(no_of_commands)):
        command = input()
        command_split = command.split(" ")
        if command_split[0] == "follow":
            network1 = follow(network1, command_split[1], command_split[2])
        elif command_split[0] == "unfollow":
            network1 = unfollow(network1, command_split[1], command_split[2])
        elif command_split[0] == "delete":
            network1 = delete_person(network1, command_split[1])

    print(network1)

if __name__ == "__main__":
    main()

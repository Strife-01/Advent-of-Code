import sys

def is_nice_string(string) -> bool:
    string = string.strip()
    is_nice = 'undefined'
    nr_1_spacesd_same_letter = 0
    length = len(string)
    list_of_pair_letters_tuple = {}
    have_dupplicates = False

    # Check for necessities
    for i in range(length - 2):
        if string[i] == string[i + 2]:
            nr_1_spacesd_same_letter += 1
    if nr_1_spacesd_same_letter < 1:
        return False
    
    for i in range(length - 1):
        list_of_pair_letters_tuple[string[i:i+2]] = list_of_pair_letters_tuple.get(string[i:i+2], 0) + 1
    for k, v in list_of_pair_letters_tuple.items():
        if v > 1:
            index = string.find(k)
            if string.find(k, index + 2, length) > 0:
                have_dupplicates = True
                break
    return have_dupplicates

with open(sys.argv[1]) as file:
    nr_nice_strings = 0
    for string in file:
        if is_nice_string(string):
            nr_nice_strings += 1
    print(nr_nice_strings)

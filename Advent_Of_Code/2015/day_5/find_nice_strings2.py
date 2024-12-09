import sys

def is_nice_string(string) -> bool:
    string = string.strip()
    is_nice = 'undefined'
    nr_1_spacesd_same_letter = 0
    length = len(string)
    have_dupplicates = False

    # Check for necessities
    for i in range(length - 2):
        if string[i] == string[i + 2]:
            nr_1_spacesd_same_letter += 1
    if nr_1_spacesd_same_letter < 1:
        return False

    for i in range(length - 1):
        if string[i:i + 2] in string[i + 2:]:
            return True
    return False


with open(sys.argv[1]) as file:
    nr_nice_strings = 0
    for string in file:
        if is_nice_string(string):
            nr_nice_strings += 1
    print(nr_nice_strings)


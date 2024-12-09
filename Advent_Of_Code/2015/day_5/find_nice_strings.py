import sys

VOWELS = 'aeiou'

# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
def contain_forbidden_combinatio(string) -> bool:
    match string:
        case 'ab' | 'cd' | 'pq' | 'xy':
            return True
        case _:
            return False

def is_nice_string(string) -> bool:
    is_nice = 'undefined'
    nr_vowels = 0
    nr_dupplicates = 0
    length = len(string)
    
    # Check for necessities
    for i in range(len(string) - 1):
        if contain_forbidden_combinatio(string[i:i+2]):
            return False
        if string[i] in VOWELS:
            nr_vowels += 1
        if string[i] == string[i + 1]:
            nr_dupplicates += 1
    if string[length - 1] in VOWELS:
        nr_vowels += 1
    
    return nr_vowels >= 3 and nr_dupplicates >= 1;

with open(sys.argv[1]) as file:
    nr_nice_strings = 0
    for string in file:
        if is_nice_string(string):
            nr_nice_strings += 1
    print(nr_nice_strings)

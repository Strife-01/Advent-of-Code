import sys


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar_cipher(charater, shift):
    return letters[(letters.index(charater) + shift) % 26]


with open(sys.argv[1]) as file:
    for line in file:
        entries = line.strip().split('-')
        list_of_words = entries[:-1]
        id, _ = entries[-1].split('[')
        id = int(id)
        copy_id = id
        id = id % 26
        deciphered = ""
        for word in list_of_words:
            w = ""
            for letter in word:
                w += cesar_cipher(letter, id)
            deciphered += " " + w
        if "north" in deciphered and "pole" in deciphered:
            print(deciphered, copy_id)

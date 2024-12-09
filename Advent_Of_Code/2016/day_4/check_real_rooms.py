import sys


sum_of_real_rooms_ids = 0
with open(sys.argv[1]) as file:
    for line in file:
        entries = line.strip().split('-')
        list_of_letters = entries[:-1]
        id_checksum = entries[-1]
        histogram_of_letters = {}
        visited = {}
        for blob_of_letters in list_of_letters:
            for letter in blob_of_letters:
                histogram_of_letters[letter] = histogram_of_letters.get(letter, 0) + 1
                visited[letter] = 0
        id, checksum = id_checksum.split('[')
        id = int(id)
        checksum = "".join(checksum[:-1])
        histogram_of_letters = sorted(histogram_of_letters.items(), key=lambda x:(-x[1], x[0]))
        top_5_letters = "".join([letter for letter, _ in histogram_of_letters[:5]])
        if top_5_letters == checksum:
            sum_of_real_rooms_ids += id

print(sum_of_real_rooms_ids)

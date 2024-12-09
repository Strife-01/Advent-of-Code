import sys
import os

# list of tuples of coordonates - starts with the begining house
visited_houses = [(0, 0)]
# index in height start
i = 0
# index in width start
j = 0

if len(sys.argv) <= 1:
    print("Usage: ./presents1.py fileName")
    sys.exit(1)

with open(sys.argv[1]) as file:
    for line in file:
        for arrow in line:
            match arrow:
                case '^':
                    i += 1
                case 'v':
                    i -= 1
                case '>':
                    j += 1
                case '<':
                    j -= 1
                case _:
                    continue
            if (i, j) not in visited_houses:
                visited_houses.append((i, j))

print(len(visited_houses))


import sys
import os

# lists of tuples of coordonates - starts with the begining house
santa_visited_houses = set()
santa_visited_houses.add((0, 0))
robo_santa_visited_houses = set()
robo_santa_visited_houses.add((0, 0))
# turn tracker
# santa = even
# robosanta = odd
turn = 0
# index in height start
i_santa, i_robosanta = 0, 0
# index in width start
j_santa, j_robosanta = 0, 0

if len(sys.argv) <= 1:
    print("Usage: ./presents1.py fileName")
    sys.exit(1)

with open(sys.argv[1]) as file:
    for line in file:
        #i_santa, i_robosanta = 0, 0
        #j_santa, j_robosanta = 0, 0
        for arrow in line:
            if turn % 2 == 0:
                match arrow:
                    case '^':
                        i_santa += 1
                    case 'v':
                        i_santa -= 1
                    case '>':
                        j_santa += 1
                    case '<':
                        j_santa -= 1
                    case _:
                        continue
                if (i_santa, j_santa) not in robo_santa_visited_houses:
                    santa_visited_houses.add((i_santa, j_santa))
            else:
                match arrow:
                    case '^':
                        i_robosanta += 1
                    case 'v':
                        i_robosanta -= 1
                    case '>':
                        j_robosanta += 1
                    case '<':
                        j_robosanta -= 1
                    case _:
                        continue
                if (i_robosanta, j_robosanta) not in santa_visited_houses:
                    robo_santa_visited_houses.add((i_robosanta, j_robosanta))
            turn += 1

#print(santa_visited_houses)
#print(robo_santa_visited_houses)
print(len(santa_visited_houses) + len(robo_santa_visited_houses) - 1)


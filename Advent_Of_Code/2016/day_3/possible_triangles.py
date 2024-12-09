import re
import sys


possible_triangles = 0


with open(sys.argv[1]) as file:
    for possible_trig in file:
        isTrig = True
        x, y, z = re.findall(r'\s*([\d]+)\s*([\d]+)\s*([\d]+)\s*', possible_trig)[0]
        x, y, z = int(x), int(y), int(z)
        if x + y <= z:
            isTrig = False
        if x + z <= y:
            isTrig = False
        if y + z <= x:
            isTrig = False
        if isTrig == True:
            possible_triangles += 1


print(possible_triangles)

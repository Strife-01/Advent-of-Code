import re
import sys


possible_triangles = 0
matrix = []


def isTriangle(x, y, z):
    isTrig = True
    if x + y <= z:
        isTrig = False
    if x + z <= y:
        isTrig = False
    if y + z <= x:
        isTrig = False
    return True if isTrig == True else False


with open(sys.argv[1]) as file:
    for possible_trig in file:
        isTrig = True
        x, y, z = re.findall(r'\s*([\d]+)\s*([\d]+)\s*([\d]+)\s*', possible_trig)[0]
        x, y, z = int(x), int(y), int(z)
        matrix.append((x, y, z))


i = 0
while i < len(matrix):
    for j in range(3):
        if (isTriangle(matrix[i][j], matrix[i+1][j], matrix[i+2][j])):
            possible_triangles += 1
    i += 3


print(possible_triangles)

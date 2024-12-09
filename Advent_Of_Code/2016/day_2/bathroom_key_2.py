import sys
grid = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]
i = 2
j = 0
code = ""


with open(sys.argv[1]) as file:
    for line in file:
        for direction in line:
            innitial_i = i
            innitial_j = j
            match direction:
                case 'U':
                    i -= 1
                    if i < 0 or grid[i][j] == None:
                        i = innitial_i
                case 'D':
                    i += 1
                    if i > 4 or grid[i][j] == None:
                        i = innitial_i
                case 'L':
                    j -= 1
                    if j < 0 or grid[i][j] == None:
                        j = innitial_j
                case 'R':
                    j += 1
                    if j > 4 or grid[i][j] == None:
                        j = innitial_j
        code += f'{grid[i][j]}'

print(code)

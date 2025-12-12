import sys
import time


CHAR_START = 'S'
CHAR_SPLIT = '^'
CHAR_EMPTY = '.'
CHAR_BEAM  = '|'


def parseData() -> list[list[str]]:
    if len(sys.argv) != 2:
        print("Usage: python3 ./main.py ./data.txt")
        sys.exit(-1)
    grid = []
    with open(sys.argv[1]) as f:
        for l in f:
            grid.append(list(l.strip()))
    return grid


def locateS(grid) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(grid[i]):
            if char == CHAR_START:
                return (i, j)


def validPosition(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()
    print()
    time.sleep(.3)


def getNrOfSplits(grid, start) -> int:
    nr_of_beams = 0
    visited = set()
    toVisit = [] # BFS
    toVisit.append(start)
    
    while len(toVisit) != 0:
        #printGrid(grid)
        (i, j) = toVisit[0]
        if (i, j) in visited:
            toVisit = toVisit[1:]
            continue
        visited.add((i, j))
        toVisit = toVisit[1:]
        if grid[i][j] == CHAR_SPLIT:
            #isActivated = False
            if (validPosition(grid, i, j + 1)) and ((i, j + 1) not in visited):# and (grid[i][j + 1] != CHAR_BEAM):
                toVisit.append((i, j + 1))
                #isActivated = True
            if (validPosition(grid, i, j - 1)) and ((i, j - 1) not in visited):# and (grid[i][j - 1] != CHAR_BEAM):
                toVisit.append((i, j - 1))
                #isActivated = True
            #if isActivated:
            nr_of_beams += 1
        elif grid[i][j] != CHAR_BEAM:
            #grid[i][j] = CHAR_BEAM
            if (validPosition(grid, i + 1, j)) and ((i + 1, j) not in visited):
                toVisit.append((i + 1, j))
    return nr_of_beams


def main():
    grid = parseData()
    start = locateS(grid)
    print(getNrOfSplits(grid, start))


if __name__ == "__main__":
    main()

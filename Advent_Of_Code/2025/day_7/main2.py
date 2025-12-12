import sys
import time


CHAR_START = 'S'
CHAR_SPLIT = '^'
CHAR_EMPTY = '.'
CHAR_BEAM  = '|'


cache = {}


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
    (i, j) = start
    while validPosition(grid, i, j) and grid[i][j] != CHAR_SPLIT:
        i += 1
    if not validPosition(grid, i, j):
        return 1
    if (i, j) in cache:
        return cache[(i, j)]
    cache[(i, j)] = getNrOfSplits(grid, (i, j - 1)) + getNrOfSplits(grid, (i, j + 1))
    return cache[(i, j)]


def main():
    grid = parseData()
    start = locateS(grid)
    print(getNrOfSplits(grid, start))


if __name__ == "__main__":
    main()

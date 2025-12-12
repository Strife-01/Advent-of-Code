import sys


neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
paperSymbol = '@'


def getPuzzleGrid():
    puzzle_grid = []
    with open(sys.argv[1]) as f:
        for line in f:
            puzzle_grid.append(list(line.strip()))
    return puzzle_grid


def isValidCoord(i, j, row_size, col_size):
    if 0 <= i < col_size and 0 <= j < row_size: return True
    return False


def parseGrid(puzzle_grid):
    nr_good_rolls = 0
    to_remove = set()
    row_size = len(puzzle_grid[0])
    col_size = len(puzzle_grid)
    for i in range(col_size):
        for j in range(row_size):
            if puzzle_grid[i][j] == paperSymbol:
                nr_papers = 0
                for di, dj in neighbors:
                    if isValidCoord(i + di, j + dj, row_size, col_size):
                        if puzzle_grid[i + di][j + dj] == paperSymbol:
                            nr_papers += 1
                            if nr_papers == 4:
                                break
                else:
                    nr_good_rolls += 1
                    to_remove.add((i,j))
    return nr_good_rolls, to_remove


def removeRolls(puzzle_grid, to_remove):
    for i, j in to_remove:
        puzzle_grid[i][j] = '.'


def getAllRemovableRolls(puzzle_grid):
    parsed = parseGrid(puzzle_grid)
    nr_rolls = 0
    while parsed[0] != 0:
        removeRolls(puzzle_grid, parsed[1])
        nr_rolls += parsed[0]
        parsed = parseGrid(puzzle_grid)
    return nr_rolls


def main():
    puzzle_grid = getPuzzleGrid()
    print(getAllRemovableRolls(puzzle_grid))


if __name__ == "__main__":
    main()

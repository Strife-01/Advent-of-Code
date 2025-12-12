import sys
#from itertools import product


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
            puzzle_grid.append(line.strip())
    return puzzle_grid


def isValidCoord(i, j, row_size, col_size):
    if i < 0 or i >= col_size or j < 0 or j >= row_size: return False
    return True


def parseGrid(puzzle_grid):
    nr_good_rolls = 0
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
    return nr_good_rolls


def main():
    puzzle_grid = getPuzzleGrid()
    print(parseGrid(puzzle_grid))


if __name__ == "__main__":
    main()

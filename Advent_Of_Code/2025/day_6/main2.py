import sys

#                   columns of numbers    operations per column
def parseData() -> tuple[list[list[int]], list[str]]:
    if len(sys.argv) != 2:
        print('Usage: python3 ./main.py ./data.txt')
        sys.exit(-1)

    numbers_grid = []

    with open(sys.argv[1]) as f:
        for l in f:
            numbers_grid.append(l.strip('\n'))
    math_operations = numbers_grid[-1].split()
    numbers_grid = numbers_grid[:-1]
    return (numbers_grid, math_operations)


def reconstructNumbers(numbers_grid):
    nrs = []
    row = []
    for j in range(len(numbers_grid[0])):
        nr = ""
        for i in range(len(numbers_grid)):
            nr += numbers_grid[i][j]
        nr = nr.strip()
        if nr != "":
            row.append(int(nr))
        else:
            nrs.append(row)
            row = []
    if len(row) != 0:
        nrs.append(row)
    return nrs


def getGrandTotal(numbers_grid, math_operations):
    numbers_grid = reconstructNumbers(numbers_grid)
    results = []
    for i, op in enumerate(math_operations):
        total = 0 if op == "+" else 1
        for j in range(len(numbers_grid[i])):
            if op == '+':
                total += numbers_grid[i][j]
            else: # op == '*'
                total *= numbers_grid[i][j]
        results.append(total)
    return sum(results)


def main():
    (numbers_grid, math_operations) = parseData()
    print(getGrandTotal(numbers_grid, math_operations))


if __name__ == "__main__":
    main()

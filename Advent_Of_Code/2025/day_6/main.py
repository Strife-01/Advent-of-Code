import sys

#                   columns of numbers    operations per column
def parseData() -> tuple[list[list[int]], list[str]]:
    if len(sys.argv) != 2:
        print('Usage: python3 ./main.py ./data.txt')
        sys.exit(-1)

    numbers_grid = []
    math_operations = []

    state = 0 # parse numbers

    with open(sys.argv[1]) as f:
        for l in f:
            line = l.strip().split()
            try:
                test = int(line[0])
                nr_line = []
                for n in line:
                    nr_line.append(int(n))
                numbers_grid.append(nr_line)
            except ValueError as e:
                math_operations = line
    return (numbers_grid, math_operations)


def getGrandTotal(numbers_grid, math_operations):
    results = []
    for i, op in enumerate(math_operations):
        total = 0 if op == "+" else 1
        for j in range(len(numbers_grid)):
            if op == '+':
                total += numbers_grid[j][i]
            else: # op == '*'
                total *= numbers_grid[j][i]
        results.append(total)
    return sum(results)


def main():
    (numbers_grid, math_operations) = parseData()
    print(getGrandTotal(numbers_grid, math_operations))


if __name__ == "__main__":
    main()

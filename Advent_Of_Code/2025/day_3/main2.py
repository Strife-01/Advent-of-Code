import sys


def getJoltage(bank: str) -> int:
    bank = bank.strip()
    nrs = []

    nr_of_digits = 12
    i_max = 0

    for current_digit in range(1, nr_of_digits + 1):
        chunk = bank[i_max:len(bank) - nr_of_digits + current_digit]
        #max_possible = sorted(chunk, reverse=True)[0]
        max_possible = max(chunk)
        index_of_dig = chunk.index(max_possible)
        i_max += index_of_dig + 1
        nrs.append(max_possible)
    return int("".join(nrs))


def main():
    sum = 0
    with open(sys.argv[1]) as f:
        for bank in f:
            sum += getJoltage(bank)

    print(sum)


if __name__ == "__main__":
    main()

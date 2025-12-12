import sys


def getJoltage(bank: str) -> int:
    bank = bank.strip()
    e1 = '1'
    e2 = '1'

    i_max = 0

    for i in range(len(bank) - 1):
        if bank[i] > e1:
            e1 = bank[i]
            i_max = i

    for i in range(i_max + 1, len(bank)):
        if bank[i] > e2:
            e2 = bank[i]

    return int(e1 + e2)


def main():
    sum = 0
    with open(sys.argv[1]) as f:
        for bank in f:
            sum += getJoltage(bank)

    print(sum)


if __name__ == "__main__":
    main()

import sys


def computePointsToZero() -> int:
    needle_point = 50
    max = 99
    min = 0

    ret = 0

    with open(sys.argv[1], "r") as file:
        for line in file:
            direction = line[0:1]
            rotations = int(line[1:])

            if direction == "L":
                needle_point -= rotations % 100
            else:
                needle_point += rotations % 100

            if needle_point < min:
                needle_point = needle_point + max + 1
            elif needle_point > max:
                needle_point = (needle_point - max) + min - 1

            if needle_point == 0:
                ret += 1

    return ret


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ./main.py data.txt")
        sys.exit(-1)
    print(computePointsToZero())


if __name__ == "__main__":
    main()

import sys


def computePointsToZero() -> int:
    needle_point = 50
    max = 99
    min = 0
    ring_size = 100

    ret = 0

    with open(sys.argv[1], "r") as file:
        for line in file:
            direction = line[0:1]
            rotations = int(line[1:])

            ret += rotations // ring_size
            ring_adder = rotations % ring_size

            target_needle_point = None

            if direction == "L":
                target_needle_point = (needle_point - ring_adder) % ring_size
                if (target_needle_point == 0 or (needle_point > 0 and target_needle_point > needle_point)):
                    ret += 1
            else:
                target_needle_point = (needle_point + ring_adder) % ring_size
                if (target_needle_point == 0 or target_needle_point < needle_point):
                    ret += 1

            needle_point = target_needle_point

    return ret


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ./main.py data.txt")
        sys.exit(-1)
    print(computePointsToZero())


if __name__ == "__main__":
    main()

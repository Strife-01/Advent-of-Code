import sys


def getRanges(file: str) -> list[list[str,str]]:
    with open(file) as f:
        return list(map(lambda s: s.strip().split('-'), f.read().split(',')))


def getInvalidNumbers(r: list[str,str]) -> list[int]:
    ret = []

    start, end = r[0], r[1]
    if len(start) == len(end) and len(start) % 2 == 1:
        return ret

    s_num = int(start)
    s_end = int(end)

    # case we have odd length nrs
    if len(start) % 2 == 1:
        start = "1" + ("0" * (len(start)))
        s_num = int(start)

    if len(end) % 2 == 1:
        end = "9" * (len(end) - 1)
        s_end = int(end)

    first_pattern = start[:len(start) // 2]
    last_pattern = end[:len(end) // 2]

    ss = int(first_pattern)
    ee = int(last_pattern)

    for i in range(ss, ee + 1):
        n = i * 10 ** len(first_pattern) + i
        if n <= s_end and n >= s_num:
            ret.append(n)
    
    return ret


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage python3 ./main.py data.txt")
        sys.exit(-1)

    ranges = getRanges(sys.argv[1])
    invalids = [sum(getInvalidNumbers(r)) for r in ranges]
    print(sum(invalids))


if __name__ == "__main__":
    main()

import sys


def getRanges(file: str) -> list[list[str,str]]:
    with open(file) as f:
        return list(map(lambda s: s.strip().split('-'), f.read().split(',')))


def getInvalidNumbers(r: list[str,str]) -> list[int]:
    ret = []

    start, end = r[0], r[1]

    s_num = int(start)
    s_end = int(end)

    set_of_pairs = []

    if len(start) == 1 and len(end) == 2:
        for i in range(11, int(end) + 1):
            if str(i) == str(i)[::-1]:
                ret.append(int(i))
        return ret

    for i in range(1, len(start) // 2 + 1):
        set_of_pairs.append(start[:i])

    index_special = i
    copy_end = end
    copy_start = start

    if len(start) < len(end):
        artificial_start = "1" + ("0" * len(start))
        for i in range(1, len(artificial_start) // 2 + 1):
            set_of_pairs.append(artificial_start[:i])
        end = "9" * len(start)

    last_pattern = end[:len(end) // 2]
    for pair in set_of_pairs:
        ss = int(pair)
        ee = int(last_pattern[:len(pair)])
        for i in range(ss, ee + 1):
            n = int(str(i) * (len(start) // len(str(i))))
            if n >= s_num and n <= s_end:
                ret.append(n)

    if len(copy_start) < len(copy_end):
        set_of_pairs = set_of_pairs[index_special:]
        start = "1" + ("0" * len(start))
        end = copy_end
        last_pattern = end[:len(end) // 2]
        for pair in set_of_pairs:
            ss = int(pair)
            ee = int(last_pattern[:len(pair)])
            for i in range(ss, ee + 1):
                n = int(str(i) * (len(start) // len(str(i))))
                if n >= s_num and n <= s_end:
                    ret.append(n)

    return list(set(ret))


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage python3 ./main.py data.txt")
        sys.exit(-1)

    ranges = getRanges(sys.argv[1])
    invalids_list = [getInvalidNumbers(r) for r in ranges]
    s = set()
    for l in invalids_list:
        for n in l:
            s.add(n)
    invalids = [sum(s)]
    print(sum(invalids))


if __name__ == "__main__":
    main()

import sys


def parseData() -> list[list[tuple[int, int]], list[int]]:
    if len(sys.argv) != 2:
        print("Usage: python3 ./main.py ./data.txt")
        sys.exit(-1)
    ret = []
    with open(sys.argv[1]) as f:
        state = 0 # 0 reading intervals 1 reading ids
        intervals = []
        ids = []
        for l in f:
            if l.strip() == "":
                state = 1
                ret.append(intervals)
                continue
            if state == 0:
                ranges = l.strip().split('-')
                intervals.append((int(ranges[0]), int(ranges[1])))
                continue
            if state == 1:
                ids.append(int(l.strip()))
        ret.append(ids)
    return ret


def overlapIntervals(intervals: list[tuple[int,int]]) -> list[tuple[int,int]]:
    # sort the list based on the first element
    intervals = sorted(intervals, key=lambda e: e[0])
    preserve = [intervals[0]]
    for i in intervals[1:]:
        last_preserved = preserve[-1]
        if last_preserved[1] >= i[0]:
            preserve[-1] = (last_preserved[0], max(i[1], last_preserved[1]))
        else:
            preserve.append(i)

    return preserve


def checkValidity(intervals: list[tuple[int,int]], ids:list[int]):
    validIds = 0
    for i in ids:
        for s, e in intervals:
            if s <= i <= e:
                validIds += 1
                break
    return validIds


def main():
    data = parseData()
    intervals = overlapIntervals(data[0])
    print(checkValidity(intervals, data[1]))


if __name__ == "__main__":
    main()

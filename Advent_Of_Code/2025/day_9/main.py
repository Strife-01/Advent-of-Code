import sys


def main():
    data = parseData()
    pottential_rectangles = getRectangles(data)
    print(max(pottential_rectangles.values()))


def getRectangles(data):
    r = {}
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            r[((x1, y1), (x2, y2))] = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    return r


def parseData():
    r = []
    with open(sys.argv[1]) as f:
        for l in f:
            [x, y] = l.strip().split(',')
            r.append((int(x), int(y)))
    return r


if __name__ == "__main__":
    main()

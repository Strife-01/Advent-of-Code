import sys


def main():
    data = parseData()
    edges = getEdges(data)
    valid_rectangles = {}

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]

            X_min = min(x1, x2)
            X_max = max(x1, x2)
            Y_min = min(y1, y2)
            Y_max = max(y1, y2)
            rectangle = (X_min, X_max, Y_min, Y_max)

            if not isIntersecting((x1 + x2) / 2, (y1 + y2) / 2, edges): continue
            if isSlicingRectangle(rectangle, edges): continue

            corner3_valid = isIntersecting(X_min, Y_max, edges) or isOnBoundary(X_min, Y_max, edges)
            corner4_valid = isIntersecting(X_max, Y_min, edges) or isOnBoundary(X_max, Y_min, edges)

            if not corner3_valid or not corner4_valid:
                continue

            valid_rectangles[rectangle] = (X_max - X_min + 1) * (Y_max - Y_min + 1)
    print(max(valid_rectangles.values()))


#ray casting
def isIntersecting(Px, Py, edges):
    intersections = 0
    for (p1_x, p1_y), (p2_x, p2_y) in edges:
        if p1_x != p2_x:
            continue
        min_y = min(p1_y, p2_y)
        max_y = max(p1_y, p2_y)
        x = p1_x

        if x > Px and min_y <= Py < max_y:
            intersections += 1

    return intersections % 2 == 1


def isSlicingRectangle(rectangle, edges):
    (X_min, X_max, Y_min, Y_max) = rectangle

    for (p1_x, p1_y), (p2_x, p2_y) in edges:
        if p1_x == p2_x and X_min < p1_x < X_max and Y_min < max(p1_y, p2_y) and min(p1_y, p2_y) < Y_max:
            return True

        if p1_y == p2_y and Y_min < p1_y < Y_max and X_min < max(p1_x, p2_x) and min(p1_x, p2_x) < X_max:
            return True

    return False


def isOnBoundary(Px, Py, edges):
    for (p1_x, p1_y), (p2_x, p2_y) in edges:
        if Px == p1_x:
            if min(p1_y, p2_y) <= Py <= max(p1_y, p2_y):
                return True
                
        if Py == p1_y:
            if min(p1_x, p2_x) <= Px <= max(p1_x, p2_x):
                return True
    return False


def getEdges(data):
    # x = column grows right, y = row grows down
    r = []
    for i in range(len(data) - 1):
        r.append(((data[i][0], data[i][1]), (data[i + 1][0], data[i + 1][1])))
    r.append(((data[-1][0], data[-1][1]), (data[0][0], data[0][1])))
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

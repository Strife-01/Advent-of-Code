import sys
import numpy as np
from itertools import product


# Minimum Spanning Tree
# Kruskal's Algorithm | Disjoint Set Union (DSU) / Union-Find


def parseInput():
    if len(sys.argv) != 2:
        print("python3 ./main.py ./data.txt")
        sys.exit(-1)

    li = []

    with open(sys.argv[1]) as f:
        for l in f:
            [x, y, z] = l.strip().split(',')
            li.append((int(x), int(y), int(z)))

    return li


def computeDistances(coordinates):
    distances = {}
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            distances[(coordinates[i], coordinates[j])] = np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2 + (coordinates[i][2] - coordinates[j][2]) ** 2)
    return distances


def initialize_dsu(coordinates):
    parent = {node: node for node in coordinates}
    size = {node: 1 for node in coordinates}
    return parent, size


def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, size, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)

    if root_i != root_j:
        if size[root_i] < size[root_j]:
            parent[root_i] = root_j
            size[root_j] += size[root_i]
        else:
            parent[root_j] = root_i
            size[root_i] += size[root_j]
        return True

    return False


def connectJunctionBoxes(parent, size, sorted_distances):
    for k in range(len(sorted_distances)):
        (coord_A, coord_B), distance = sorted_distances[k]
        successful = union(parent, size, coord_A, coord_B)

        if successful and max(size.values()) == len(parent):
            return coord_A[0] * coord_B[0]
    return None


def main():
    coordinates = parseInput()
    distances = computeDistances(coordinates)
    sorted_distances = sorted(distances.items(), key=lambda e: e[1])
    parent, size = initialize_dsu(coordinates)
    print(connectJunctionBoxes(parent, size, sorted_distances))


if __name__ == "__main__":
    main()

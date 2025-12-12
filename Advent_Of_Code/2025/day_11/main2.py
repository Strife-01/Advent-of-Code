import sys
import copy
from functools import cache


sys.setrecursionlimit(20000)


def main():
    data = parseData()
    print(part_2(data))


def part_2(data):
    @cache
    def get_nr_paths(node, target):
        if node == target:
            return 1
        if node not in data:
            return 0
        total = 0
        for v in data[node]:
            total += get_nr_paths(v, target)
        return total

    t_1 = get_nr_paths("fft", "dac")
    t_2 = get_nr_paths("dac", "fft")

    if t_1 > 0:
        return get_nr_paths("svr", "fft") * t_1 * get_nr_paths("dac", "out")
    return get_nr_paths("svr", "out") * t_2 * get_nr_paths("fft", "out")


def parseData():
    ret = {}
    with open(sys.argv[1]) as f:
        for l in f:
            [k, v] = l.strip().split(': ')
            ret[k] = v.split(' ')
    return ret


if __name__ == "__main__":
    main()

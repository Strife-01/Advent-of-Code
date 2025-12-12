import sys


def main():
    data = parseData()
    part_1(data)


def reccursiveStep(current_key, data):
    total = 0
    for pottential in data[current_key]:
        if pottential == "out": total += 1
        else:
            total += reccursiveStep(pottential, data)
    return total


def part_1(data):
    #nr_paths = 0
    print(reccursiveStep("you", data))


def parseData():
    ret = {}
    with open(sys.argv[1]) as f:
        for l in f:
            [k, v] = l.strip().split(': ')
            ret[k] = v.split(' ')
    return ret


if __name__ == "__main__":
    main()

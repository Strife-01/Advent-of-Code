import sys
if len(sys.argv) < 2:
    print('Usage: ./surfaceArea.py fileName')
total_paper = 0
with open(sys.argv[1]) as file:
    for line in file:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        total_paper += l * w * h
        min1, min2, _ = sorted([l, w, h])
        total_paper += 2 * (min1 + min2)

print(total_paper)

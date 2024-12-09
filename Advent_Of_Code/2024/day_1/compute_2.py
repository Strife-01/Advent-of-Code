multiplicity = {}
multiplicity_in_1 = {}
with open("input2.txt") as file:
    for line in file:
        line_vals = line.split("   ")
        multiplicity[int(line_vals[0])] = 0
        multiplicity_in_1[int(line_vals[0])] = multiplicity_in_1.get(int(line_vals[0]), 0) + 1

with open("input2.txt") as file:
    for line in file:
        line_vals = line.split("   ")
        if multiplicity_in_1.get(int(line_vals[1]), 0) != 0:
            multiplicity[int(line_vals[1])] = multiplicity.get(int(line_vals[1]), 0) + 1

print(multiplicity)
print(multiplicity_in_1)

total = 0
for k, v in multiplicity_in_1.items():
    total += k * v * multiplicity[k]

print(total)

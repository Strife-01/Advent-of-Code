nr_of_safe_levels = 0
with open("dataset1.txt") as file:
    for line in file:
        line_values = line.split(" ")
        length = len(line_values)
        for i in range(length):
            line_values[i] = int(line_values[i])
        isSafe = True
        for i in range(length - 2):
            if abs(line_values[i] - line_values[i + 1]) < 1 or abs(line_values[i] - line_values[i + 1]) > 3:
                isSafe = False
                break
            elif line_values[i] < line_values[i + 1] and line_values[i + 1] >= line_values[i + 2]:
                isSafe = False
                break
            elif line_values[i] > line_values[i + 1] and line_values[i + 1] <= line_values[i + 2]:
                isSafe = False
                break
        if abs(line_values[length - 2] - line_values[length - 1]) < 1 or abs(line_values[length - 2] - line_values[length - 1]) > 3:
            isSafe = False
        elif line_values[length - 2] < line_values[length - 1] and line_values[length - 3] >= line_values[length - 2]:
            isSafe = False
        elif line_values[length - 2] > line_values[length - 1] and line_values[length - 3] <= line_values[length - 2]:
            isSafe = False
        if isSafe == True:
            nr_of_safe_levels += 1
        print(line_values, isSafe)

print(nr_of_safe_levels)

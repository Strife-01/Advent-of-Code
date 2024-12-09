with open("input.txt") as file:
    total_sum = 0
    list_left = []
    list_right = []
    for line in file:
        line_nums = line.split('   ')
        list_left.append(int(line_nums[0]))
        list_right.append(int(line_nums[1]))
    list_left = sorted(list_left)
    list_right = sorted(list_right)
    for i in range(len(list_left)):
        total_sum += abs(list_left[i] - list_right[i])
    print(total_sum)


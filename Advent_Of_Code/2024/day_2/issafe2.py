nr_of_safe_levels = 0

def checkSafety(line_values, length):
    unsafeIndices = set()
    isSafe = True
    for i in range(length - 2):
        if abs(line_values[i] - line_values[i + 1]) < 1 or abs(line_values[i] - line_values[i + 1]) > 3:
            isSafe = False
            unsafeIndices.add(i)
            unsafeIndices.add(i + 1)
        elif line_values[i] < line_values[i + 1] and line_values[i + 1] >= line_values[i + 2]:
            isSafe = False
            unsafeIndices.add(i)
            unsafeIndices.add(i + 1)
            unsafeIndices.add(i + 2)
        elif line_values[i] > line_values[i + 1] and line_values[i + 1] <= line_values[i + 2]:
            isSafe = False
            unsafeIndices.add(i)
            unsafeIndices.add(i + 1)
            unsafeIndices.add(i + 2)
    if abs(line_values[length - 2] - line_values[length - 1]) < 1 or abs(line_values[length - 2] - line_values[length - 1]) > 3:
        isSafe = False
        unsafeIndices.add(length - 1)
        unsafeIndices.add(length - 2)
    elif line_values[length - 2] < line_values[length - 1] and line_values[length - 3] >= line_values[length - 2]:
        isSafe = False
        unsafeIndices.add(length - 1)
        unsafeIndices.add(length - 2)
        unsafeIndices.add(length - 3)
    elif line_values[length - 2] > line_values[length - 1] and line_values[length - 3] <= line_values[length - 2]:
        isSafe = False
        unsafeIndices.add(length - 1)
        unsafeIndices.add(length - 2)
        unsafeIndices.add(length - 3)
    #if isSafe == True:
        #print(line_values, isSafe)
    return [isSafe, unsafeIndices]

def checkNormalSafety(line_values, length):
    isNowSafe = True
    for i in range(length - 2):
        if abs(line_values[i] - line_values[i + 1]) < 1 or abs(line_values[i] - line_values[i + 1]) > 3:
            isNowSafe = False
            print(i)
            break
        elif line_values[i] < line_values[i + 1] and line_values[i + 1] >= line_values[i + 2]:
            isNowSafe = False
            print(i)
            break    
        elif line_values[i] > line_values[i + 1] and line_values[i + 1] <= line_values[i + 2]:
            isNowSafe = False
            print(i)
            break
    if abs(line_values[length - 2] - line_values[length - 1]) < 1 or abs(line_values[length - 2] - line_values[length - 1]) > 3:
        isNowSafe = False
        print(i)
    elif line_values[length - 2] < line_values[length - 1] and line_values[length - 3] >= line_values[length - 2]:
        isNowSafe = False
        print(i)
    elif line_values[length - 2] > line_values[length - 1] and line_values[length - 3] <= line_values[length - 2]:
        isNowSafe = False
        print(i)
    print(line_values, isNowSafe)
    return isNowSafe



def removeIndexIFromList(arr, length, index):
    copy = list(arr)
    del copy[index]
    return [copy, length - 1]

with open("dataset1.txt") as file:
    for line in file:
        line_values = line.split(" ")
        length = len(line_values)
        for i in range(length):
            line_values[i] = int(line_values[i])
        safeTest, unsafeIndices = checkSafety(line_values, length)
        if safeTest:
            nr_of_safe_levels += 1
        else:
            for removeIndex in unsafeIndices:
                checkList, l = removeIndexIFromList(line_values, length, removeIndex)
                if checkNormalSafety(checkList, l):
                    nr_of_safe_levels += 1
                    break
        
print(nr_of_safe_levels)

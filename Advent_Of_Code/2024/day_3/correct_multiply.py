import re
import sys


def find_mul(string) -> str:
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', string)


def compute(command) -> int:
    if command.startswith('mul'):
        x, y = command[3:].split(',')
        # exclude paranthesis
        return int(x[1:]) * int(y[:-1])


#test
#TEST = find_mul('xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))')
#print(TEST)


total = 0


with open(sys.argv[1]) as file:
    #commands = TEST
    commands = find_mul(file.read())
    active = True
    for command in commands:
        if command == 'do()':
            active = True
        elif command == 'don\'t()':
            active = False
        else:
            if active == True:
                total += compute(command)


print(total)

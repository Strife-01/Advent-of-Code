import re
import sys
import numpy


GRID_HEIGHT = 1000
GRID_WIDTH = 1000
grid = numpy.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)


def extract_command_plus_coordinates_from_command(command) -> list[str, list[int], list[int]]:
    command, coord_start, coord_end = re.findall(r'(turn on|toggle|turn off)+[\D]*(\d+,\d+)+[\D]*(\d+,\d+)+', command)[0]
    return [command, coord_start.split(','), coord_end.split(',')]


'''
TEST ONLY
print(extract_command_plus_coordinates_from_command('turn on 0,0 through 999,999'))
print(extract_command_plus_coordinates_from_command('toggle 0,0 through 999,0'))
print(extract_command_plus_coordinates_from_command('turn off 499,499 through 500,500'))
'''


with open(sys.argv[1]) as commands:
    for command in commands:
        com, coord_start, coord_end = extract_command_plus_coordinates_from_command(command)

        for i in range(int(coord_start[0]), int(coord_end[0]) + 1):
            for j in range(int(coord_start[1]), int(coord_end[1]) + 1):
                if com == 'turn on':
                    grid[i][j] += 1
                elif com == 'turn off':
                    grid[i][j] -= 1
                    if grid[i][j] < 0:
                        grid[i][j] = 0
                else:
                    grid[i][j] += 2


total_brightness_leds = 0
for i in range(GRID_HEIGHT):
    for j in range(GRID_WIDTH):
        total_brightness_leds += grid[i][j]


print(total_brightness_leds)

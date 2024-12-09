import sys
import copy


UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
OBSTACLE = '#'

# obstruction ahead ==> turn right 90 deg :else: step forward


def clean_line(line:str) -> str:
    return line.strip()


def locate_guard(map:list[str]) -> list[tuple[int, int], str]:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in [UP, DOWN, LEFT, RIGHT]:
                return [(i, j), map[i][j]]


def move_untill_obstacle(map, postition, direction):
    moved_position = 0
    i, j = postition
    if direction == UP:
        start = i
        end = -1
        step = -1
        mutate = "i"
    elif direction == DOWN:
        start = i
        end = len(map)
        step = 1
        mutate = "i"
    elif direction == LEFT:
        start = j
        end = -1
        step = -1
        mutate = "j"
    elif direction == RIGHT:
        start = j
        end = len(map[i])
        step = 1
        mutate = "j"

    if mutate == "i":
        for index_i in range(start, end, step):
            if map[index_i][j] == OBSTACLE:
                return moved_position - 1
            moved_position += 1
        return moved_position
    elif mutate == "j":
        for index_j in range(start, end, step):
            if map[i][index_j] == OBSTACLE:
                return moved_position - 1
            moved_position += 1
        return moved_position


def get_distinct_visited_locations(map:list[str], starting_position:tuple[int, int], guard_start_direction:str) -> set[tuple[int, int]]:
    unique_visited_locations = set()
    unique_visited_locations_plus_direction = set()
    bound_up = 0
    bound_down = len(map) - 1
    bound_left = 0
    bound_right = len(map[0]) - 1
    i, j = starting_position
    guard_direction = guard_start_direction
    last_added = None
    while i >= bound_up and i <= bound_down and j >= bound_left and j <= bound_right:
        unique_visited_locations.add((i, j))
        unique_visited_locations_plus_direction.add((i, j, guard_direction))
        last_added = (i, j)
        taken_steps = move_untill_obstacle(map, (i, j), guard_direction)
        match guard_direction:
            case '^':
                for index_i in range(i - 1, i - (taken_steps + 1), -1):
                    if (index_i, j, guard_direction) in unique_visited_locations_plus_direction:
                        return "loop"
                    unique_visited_locations.add((index_i, j))
                    unique_visited_locations_plus_direction.add((index_i, j, guard_direction))
                    last_added = (index_i, j)
                guard_direction = RIGHT
                i = i - taken_steps
            case 'v':
                for index_i in range(i + 1, i + taken_steps + 1):
                    if (index_i, j, guard_direction) in unique_visited_locations_plus_direction:
                        return "loop"
                    unique_visited_locations.add((index_i, j))
                    unique_visited_locations_plus_direction.add((index_i, j, guard_direction))
                    last_added = (index_i, j)
                guard_direction = LEFT
                i = i + taken_steps
            case '<':
                for index_j in range(j - 1, j - (taken_steps + 1), -1):
                    if (i, index_j, guard_direction) in unique_visited_locations_plus_direction:
                        return "loop"
                    unique_visited_locations.add((i, index_j))
                    unique_visited_locations_plus_direction.add((i, index_j, guard_direction))
                    last_added = (i, index_j)
                guard_direction = UP
                j = j - taken_steps
            case '>':
                for index_j in range(j + 1, j + taken_steps + 1):
                    if (i, index_j, guard_direction) in unique_visited_locations_plus_direction:
                        return "loop"
                    unique_visited_locations.add((i, index_j))
                    unique_visited_locations_plus_direction.add((i, index_j, guard_direction))
                    last_added = (i, index_j)
                guard_direction = DOWN
                j = j + taken_steps
        if guard_direction == guard_start_direction and (i, j) == starting_position:
            print("loop")
            return "loop"
    
    # to correct off by one
    if last_added[0] < 0 or last_added[0] >= len(map) or last_added[1] < 0 or last_added[1] >= len(map[0]):
        unique_visited_locations.remove(last_added)

    return unique_visited_locations


with open(sys.argv[1]) as file:
    map:list[str] = []
    nr_of_possible_blockades = 0
    for line in file:
        map.append(clean_line(line))
    guard_position, guard_direction = locate_guard(map)
    unique_visited_locations = get_distinct_visited_locations(map, guard_position, guard_direction)
    sorted_unique_visited_locations = sorted(unique_visited_locations, key=lambda t: (t[0], t[1]))
    for i, j in sorted_unique_visited_locations:
        if (i, j) != guard_direction:
            map_copy = copy.deepcopy(map)
            map_copy[i] = map_copy[i][:j] + '#' + map_copy[i][j + 1:]
            if (get_distinct_visited_locations(map_copy, guard_position, guard_direction) == "loop"):
                nr_of_possible_blockades += 1

    print(nr_of_possible_blockades)


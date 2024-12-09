import sys

# Use Manhattan distance
i = 0  # vertical axis (North/South)
j = 0  # horizontal axis (East/West)

# Initial direction (starting facing North)
direction = 'North'

# Read directions from file
with open(sys.argv[1]) as directions:
    directions = directions.read().strip().split(', ')  # Read and split directions by ', '
    visited = set()  # Set to store visited coordinates
    visited.add((i, j))  # Start at the origin (0, 0)
    
    for d in directions:
        dir = d[0]  # 'R' or 'L'
        step = int(d[1:])  # number of steps to move
        
        # Turn right ('R') or left ('L')
        if dir == 'R':
            if direction == 'North':
                direction = 'East'
            elif direction == 'East':
                direction = 'South'
            elif direction == 'South':
                direction = 'West'
            elif direction == 'West':
                direction = 'North'
        
        elif dir == 'L':
            if direction == 'North':
                direction = 'West'
            elif direction == 'West':
                direction = 'South'
            elif direction == 'South':
                direction = 'East'
            elif direction == 'East':
                direction = 'North'

        # Move step by step in the current direction
        for _ in range(step):
            if direction == 'North':
                i += 1
            elif direction == 'South':
                i -= 1
            elif direction == 'East':
                j += 1
            elif direction == 'West':
                j -= 1

            # Check if the current coordinate has been visited
            if (i, j) in visited:
                print(f"The first location visited twice is ({i}, {j})")
                print(f"Manhattan distance: {abs(i) + abs(j)}")
                sys.exit(0)  # Stop the program after finding the first repeated location
            visited.add((i, j))



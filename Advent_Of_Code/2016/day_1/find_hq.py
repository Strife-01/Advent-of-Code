import sys

# Use Manhattan distance
i = 0  # direction up/down (North/South)
j = 0  # direction left/right (East/West)

# Initial direction (starting facing North)
direction = 'North'

# Read directions from file
with open(sys.argv[1]) as directions:
    directions = directions.read().strip().split(', ')  # Read and split directions by ', '
    
    for d in directions:
        dir = d[0]  # 'R' or 'L'
        step = int(d[1:])  # steps to move
        
        if dir == 'R':  # Turn right
            if direction == 'North':
                direction = 'East'
                j += step
            elif direction == 'East':
                direction = 'South'
                i -= step
            elif direction == 'South':
                direction = 'West'
                j -= step
            elif direction == 'West':
                direction = 'North'
                i += step
        elif dir == 'L':  # Turn left
            if direction == 'North':
                direction = 'West'
                j -= step
            elif direction == 'West':
                direction = 'South'
                i -= step
            elif direction == 'South':
                direction = 'East'
                j += step
            elif direction == 'East':
                direction = 'North'
                i += step

# Calculate Manhattan distance from origin (0, 0)
print(abs(i) + abs(j))


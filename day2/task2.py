with open('directions.txt') as directions_file:
    directions_array = directions_file.readlines()

directions_array = [direction.split() for direction in directions_array] 

starting_position = 0
starting_depth = 0
aim = 0

for direction in directions_array:
    if direction[0] == 'forward':
        starting_position += int(direction[1])
        starting_depth += (int(direction[1]) * aim)
    elif direction[0] == 'down':
        aim += int(direction[1])
    elif direction[0] == 'up':
        aim -= int(direction[1])

print(starting_depth * starting_position)

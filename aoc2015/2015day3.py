f = open('2015day3.txt', 'r')
strings = f.read().splitlines()
f.close()

map_grid = {}  # it follows{ 'location': number_of_presents_received }

lucky_children_count = 0
map_grid[str([0, 0])] = 1
curr_coords = [0, 0]  # it follows that the bottom left is 0,0
for i in range(0, len(strings[0])):
    if strings[0][i] == '^':
        curr_coords[1] += 1
    elif strings[0][i] == '>':
        curr_coords[0] += 1
    elif strings[0][i] == 'v':
        curr_coords[1] -= 1
    elif strings[0][i] == '<':
        curr_coords[0] -= 1

    if str(curr_coords) not in map_grid:
        map_grid[str(curr_coords)] = 1
        if map_grid[str(curr_coords)] >= 1:
            lucky_children_count += 1
    else:
        map_grid[str(curr_coords)] += 1
        # if map_grid[str(curr_coords)] >=1:
        #     lucky_children_count += 1

print(lucky_children_count + 1)

# part 2

map_grid = {}  # it follows{ 'location': number_of_presents_received }

lucky_children_count = 0
map_grid[str([0, 0])] = 1
curr_coords = [[0, 0], [0, 0]]  # it follows that the bottom left is 0,0, [santa_coord, robo_santa_coord]

for i in range(0, len(strings[0])):
    if strings[0][i] == '^':
        curr_coords[i % 2][1] += 1
    elif strings[0][i] == '>':
        curr_coords[i % 2][0] += 1
    elif strings[0][i] == 'v':
        curr_coords[i % 2][1] -= 1
    elif strings[0][i] == '<':
        curr_coords[i % 2][0] -= 1

    if str(curr_coords[i % 2]) not in map_grid:
        map_grid[str(curr_coords[i % 2])] = 1
        if map_grid[str(curr_coords[i % 2])] >= 1:
            lucky_children_count += 1
    else:
        map_grid[str(curr_coords[i % 2])] += 1
        # if map_grid[str(curr_coords)] >=1:
        #     lucky_children_count += 1

print(lucky_children_count + 1)

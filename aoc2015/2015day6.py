f = open('2015day6.txt', 'r')
strings = f.read().splitlines()
f.close()

# parse input
operations = []
for entry in strings:
    operation = []  # follows format of [what to do, from where, to where]
    if 'turn on' in entry:
        operation.append(0)
    elif 'turn off' in entry:
        operation.append(1)
    elif 'toggle' in entry:
        operation.append(2)

    coords = entry.replace('turn on ', '').replace('turn off ', '').replace('toggle ', '').split(' through ')
    operation.append(coords[0].split(','))
    operation[1][0] = int(operation[1][0])
    operation[1][1] = int(operation[1][1])
    operation.append(coords[1].split(','))
    operation[2][0] = int(operation[2][0])
    operation[2][1] = int(operation[2][1])
    operations.append(operation)

grid = []
for i in range(0, 1000):
    grid.append([])
    for j in range(0, 1000):
        grid[i].append(0)


def turn_on(g: [], coord_from: [], coord_to: []) -> []:
    for i in range(coord_from[0], coord_to[0] + 1):
        for j in range(coord_from[1], coord_to[1] + 1):
            g[i][j] += 1
    return g


def turn_off(g: [], coord_from: [], coord_to: []) -> []:
    for i in range(coord_from[0], coord_to[0] + 1):
        for j in range(coord_from[1], coord_to[1] + 1):
            g[i][j] -= 1
            if g[i][j] < 0:
                g[i][j] = 0
            # g[i][j] = 0
    return g


def toggle(g: [], coord_from: [], coord_to: []) -> []:
    for i in range(coord_from[0], coord_to[0] + 1):
        for j in range(coord_from[1], coord_to[1] + 1):
            g[i][j] += 2
            # if g[i][j] == 0:
            #     g[i][j] = 1
            # else:
            #     g[i][j] = 0
    return g


def count_lights(g: []) -> int:
    count = 0
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            if g[i][j] == 1:
                count += 1
    return count


def count_brightness(g: []) -> int:
    count = 0
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            count += g[i][j]
    return count


def print_lights(g: []):
    for i in range(0, len(g)):
        for j in range(0, len(g[0])):
            print(g[i][j], end='')
        print('\n', end='')


for i in range(0, len(operations)):
    if operations[i][0] == 0:
        grid = turn_on(grid, operations[i][1], operations[i][2])
    if operations[i][0] == 1:
        grid = turn_off(grid, operations[i][1], operations[i][2])
    if operations[i][0] == 2:
        grid = toggle(grid, operations[i][1], operations[i][2])

# print_lights(grid)
print(count_brightness(grid))
pass

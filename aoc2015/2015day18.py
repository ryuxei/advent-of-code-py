f = open('2015day18.txt', 'r')
strings = f.read().splitlines()
f.close()


def do_iteration(grid: list) -> list:
    new_grid = []
    for i in range(0, 100):
        new_grid.append([])
        for j in range(0, 100):
            neighbor_count = 0
            if i != 0 and grid[i - 1][j] == '#':
                neighbor_count += 1
            if i != 0 and j != 99 and grid[i - 1][j + 1] == '#':
                neighbor_count += 1
            if j != 99 and grid[i][j + 1] == '#':
                neighbor_count += 1
            if i != 99 and j != 99 and grid[i + 1][j + 1] == '#':
                neighbor_count += 1
            if i != 99 and grid[i + 1][j] == '#':
                neighbor_count += 1
            if i != 99 and j != 0 and grid[i + 1][j - 1] == '#':
                neighbor_count += 1
            if j != 0 and grid[i][j - 1] == '#':
                neighbor_count += 1
            if i != 0 and j != 0 and grid[i - 1][j - 1] == '#':
                neighbor_count += 1

            if i == 0 and j == 0:
                new_grid[i].append('#')
            elif i == 0 and j == 99:
                new_grid[i].append('#')
            elif i == 99 and j == 0:
                new_grid[i].append('#')
            elif i == 99 and j == 99:
                new_grid[i].append('#')
            elif grid[i][j] == '#':
                if neighbor_count == 2 or neighbor_count == 3:
                    new_grid[i].append('#')
                else:
                    new_grid[i].append('.')
            elif grid[i][j] == '.':
                if neighbor_count == 3:
                    new_grid[i].append('#')
                else:
                    new_grid[i].append('.')
    return new_grid


def count_lights_on(grid: list) -> int:
    count = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if grid[i][j] == '#':
                count += 1
    return count


light_grid = []

for i in range(0, 100):
    light_grid.append([])
    for j in range(0, 100):
        light_grid[i].append(strings[i][j])

for i in range(0, 100):
    light_grid = do_iteration(light_grid)

print(count_lights_on(light_grid))

pass

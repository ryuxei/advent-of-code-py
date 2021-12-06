def do_part_1(s: list):
    grid = make_grid()

    for instruction in s:
        start = [int(a) for a in instruction.split(' -> ')[0].split(',')]
        end = [int(a) for a in instruction.split(' -> ')[1].split(',')]
        if start[0] == end[0] or start[1] == end[1]:
            draw_line(start, end, grid)

    print(count_multiple_intersects(grid))

    return


def do_part_2(s: list):
    grid = make_grid()

    for instruction in s:
        start = [int(a) for a in instruction.split(' -> ')[0].split(',')]
        end = [int(a) for a in instruction.split(' -> ')[1].split(',')]
        draw_line(start, end, grid)

    print(count_multiple_intersects(grid))

    return


def make_grid() -> list:
    grid = []
    for i in range(0, 1000):
        grid.append([])
        for j in range(0, 1000):
            grid[i].append(0)
    return grid


def draw_line(start, end, grid):
    i_step = 1 if start[0] <= end[0] else -1
    j_step = 1 if start[1] <= end[1] else -1
    i = start[0]
    j = start[1]
    while i != end[0] or j != end[1]:
        grid[i][j] += 1
        if i != end[0]:
            i += i_step
        if j != end[1]:
            j += j_step
    grid[i][j] += 1
    return


def count_multiple_intersects(grid) -> int:
    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if grid[i][j] >= 2:
                count += 1
    return count


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()
    do_part_1(input_str)
    do_part_2(input_str)
    pass

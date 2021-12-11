def do_part_1(s: list):
    ogrid, flash_grid = gen_octopus_grid(s)
    flash_count = 0
    for step in range(1, 101000): # change to 101 for part 1
        new_flash_count = do_step(ogrid, flash_grid)

        # part 2
        if new_flash_count == 100:
            print('step', step)
            break

        flash_count += new_flash_count
    print('flash_count', flash_count)
    return


def do_part_2(s: list):
    return


def gen_octopus_grid(s) -> list:
    ogrid = []
    flash_grid = []
    for i in range(0, len(s)):
        ogrid.append([])
        flash_grid.append([])
        for j in range(0, len(s[0])):
            ogrid[i].append(int(s[i][j]))
            flash_grid[i].append(0)
    return [ogrid, flash_grid]


def do_step(ogrid, fgrid) -> int:
    flash_count = 0
    flash_list = []
    for i in range(0, len(ogrid)):
        for j in range(0, len(ogrid[0])):
            ogrid[i][j] += 1
            if ogrid[i][j] > 9:
                flash_list.append([i, j])

    i = 0
    while i < len(flash_list):
        adj_coords = get_adjacent_coords(flash_list[i])
        for c in adj_coords:
            ogrid[c[0]][c[1]] += 1
            if ogrid[c[0]][c[1]] > 9 and [c[0], c[1]] not in flash_list:
                flash_list.append([c[0], c[1]])
        fgrid[flash_list[i][0]][flash_list[i][1]] = 1
        flash_count += 1
        i += 1

    for i in range(0, len(ogrid)):
        for j in range(0, len(ogrid[0])):
            ogrid[i][j] = 0 if ogrid[i][j] > 9 else ogrid[i][j]
            fgrid[i][j] = 0

    return flash_count


def get_adjacent_coords(coord) -> list:
    adj_coords = []

    if coord[0] != 0:
        if coord[1] != 0:
            adj_coords.append([coord[0] - 1, coord[1] - 1])
        adj_coords.append([coord[0] - 1, coord[1]])
        if coord[1] != 9:
            adj_coords.append([coord[0] - 1, coord[1] + 1])
    if coord[1] != 9:
        adj_coords.append([coord[0], coord[1] + 1])
        if coord[0] != 9:
            adj_coords.append([coord[0] + 1, coord[1] + 1])
    if coord[0] != 9:
        adj_coords.append([coord[0] + 1, coord[1]])
        if coord[1] != 0:
            adj_coords.append([coord[0] + 1, coord[1] - 1])
    if coord[1] != 0:
        adj_coords.append([coord[0], coord[1] - 1])

    return adj_coords


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

def do_part_1(s: list):
    office_map = gen_office_map(int(s[0]), 40, 40)
    distance_map = gen_distance_map(office_map)
    print(distance_map[39][31])
    return


def do_part_2(s: list):
    office_map = gen_office_map(int(s[0]), 200, 200)  # better safe than sorry lol
    distance_map = gen_distance_map(office_map)
    how_many_in_50 = 0
    for i in range(0, len(distance_map)):
        for j in range(0, len(distance_map[0])):
            if 1 <= distance_map[i][j] <= 50:
                # we dont do 0<=x<=50 cuz some area of the office might be completely sealed
                # off, so their dist will remain at zero and we dont want to count them.
                how_many_in_50 += 1

    print(how_many_in_50 + 1)  # including the start
    return


def gen_office_map(fav_num, width, height) -> list:
    m = []
    for i in range(0, height):
        m.append([])
        for j in range(0, width):
            n = (j * j) + (3 * j) + (2 * j * i) + (i) + (i * i) + fav_num
            binary_repr = [int(a) for a in bin(n)[2:]]
            m[i].append(sum(binary_repr) % 2)
    return m


def gen_distance_map(office_map) -> list:
    m = []
    for i in range(0, len(office_map)):
        m.append([])
        for j in range(0, len(office_map[0])):
            if office_map[i][j] != 1:
                m[i].append(0)
            else:
                m[i].append(-1)

    adjacent_coords = [[1, 1]]
    curr_distance = 0

    while len(adjacent_coords) > 0:
        new_coords = []
        for a in adjacent_coords:
            m[a[0]][a[1]] = curr_distance
            if a[0] != 0 and m[a[0] - 1][a[1]] == 0 and \
                    [a[0] - 1, a[1]] not in new_coords and [a[0] - 1, a[1]] != [1, 1]:
                new_coords.append([a[0] - 1, a[1]])
            if a[0] != len(office_map) - 1 and m[a[0] + 1][a[1]] == 0 and \
                    [a[0] + 1, a[1]] not in new_coords and [a[0] + 1, a[1]] != [1, 1]:
                new_coords.append([a[0] + 1, a[1]])
            if a[1] != 0 and m[a[0]][a[1] - 1] == 0 and \
                    [a[0], a[1] - 1] not in new_coords and [a[0], a[1] - 1] != [1, 1]:
                new_coords.append([a[0], a[1] - 1])
            if a[1] != len(office_map[0]) - 1 and m[a[0]][a[1] + 1] == 0 and \
                    [a[0], a[1] + 1] not in new_coords and [a[0], a[1] + 1] != [1, 1]:
                new_coords.append([a[0], a[1] + 1])
        adjacent_coords = new_coords
        curr_distance += 1

    return m


if __name__ == '__main__':
    input_str = ['1362']
    do_part_1(input_str)
    do_part_2(input_str)

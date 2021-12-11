def do_part_1(s: list):
    m, objectives = gen_map(s)
    objectives.sort(key=lambda a: int(a[0]))
    distance_list = []
    for o in objectives:
        d = []
        dist_map = gen_distance_map(m, [o[1], o[2]])
        for i in range(0, len(objectives)):
            d.append(dist_map[objectives[i][1]][objectives[i][2]])
        distance_list.append(d)

    shortest_path = [0, 2, 1, 3, 6, 4, 5, 7, 0]
    shortest_distance = cal_distance(shortest_path, distance_list)

    possible_paths = [[0]]
    while len(possible_paths) != 0:
        curr_path = possible_paths[0]
        points_visited = 0

        for i in range(1, 8):
            if i in curr_path:
                points_visited += 1

        if points_visited == 7 and curr_path[-1] == 0:
            distance = cal_distance(curr_path, distance_list)
            if distance <= shortest_distance:
                shortest_path = curr_path
                shortest_distance = distance
        else:
            distance = cal_distance(curr_path, distance_list)
            if distance < shortest_distance:
                new_paths = []
                for i in range(0, 8):
                    if i != curr_path[-1]:
                        if cal_distance(curr_path + [i], distance_list) < shortest_distance:
                            new_paths.append(curr_path + [i])
                possible_paths += new_paths

        possible_paths.pop(0)
        print(distance, curr_path, len(possible_paths), shortest_distance, shortest_path)

    print(shortest_distance, shortest_path)
    return


def cal_distance(path, d_list) -> int:
    d = 0
    for i in range(0, len(path) - 1):
        d += d_list[path[i]][path[i + 1]]
    return d


def do_part_2(s: list):
    return


def gen_map(s) -> list:
    m = []
    objectives = []
    for i in range(0, len(s)):
        m.append([])
        for j in range(0, len(s[0])):
            if s[i][j] == '#':
                m[i].append(1)
            else:
                m[i].append(0)
                if s[i][j] in '012345678':
                    objectives.append([s[i][j], i, j])
    return [m, objectives]


def gen_distance_map(reg_map, starting_coords) -> list:
    m = []
    for i in range(0, len(reg_map)):
        m.append([])
        for j in range(0, len(reg_map[0])):
            if reg_map[i][j] != 1:
                m[i].append(0)
            else:
                m[i].append(-1)

    adjacent_coords = [starting_coords]
    curr_distance = 0

    while len(adjacent_coords) > 0:
        new_coords = []
        for a in adjacent_coords:
            m[a[0]][a[1]] = curr_distance
            if a[0] != 0 and m[a[0] - 1][a[1]] == 0 and \
                    [a[0] - 1, a[1]] not in new_coords and [a[0] - 1, a[1]] != starting_coords:
                new_coords.append([a[0] - 1, a[1]])
            if a[0] != len(reg_map) - 1 and m[a[0] + 1][a[1]] == 0 and \
                    [a[0] + 1, a[1]] not in new_coords and [a[0] + 1, a[1]] != starting_coords:
                new_coords.append([a[0] + 1, a[1]])
            if a[1] != 0 and m[a[0]][a[1] - 1] == 0 and \
                    [a[0], a[1] - 1] not in new_coords and [a[0], a[1] - 1] != starting_coords:
                new_coords.append([a[0], a[1] - 1])
            if a[1] != len(reg_map[0]) - 1 and m[a[0]][a[1] + 1] == 0 and \
                    [a[0], a[1] + 1] not in new_coords and [a[0], a[1] + 1] != starting_coords:
                new_coords.append([a[0], a[1] + 1])
        adjacent_coords = new_coords
        curr_distance += 1

    return m


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

def do_part_1(s: list):
    sum_of_low_point = 0
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            num = int(s[i][j])
            up = int(s[i - 1][j]) if i != 0 else 10
            left = int(s[i][j - 1]) if j != 0 else 10
            down = int(s[i + 1][j]) if i != len(s) - 1 else 10
            right = int(s[i][j + 1]) if j != len(s[0]) - 1 else 10

            if num < min(up, down, left, right):
                sum_of_low_point += num + 1

    print(sum_of_low_point)
    return


def do_part_2(s: list):
    map = []
    basin_mark = []
    for i in range(0, len(s)):
        map.append([])
        basin_mark.append([])
        for j in range(0, len(s[0])):
            map[i].append(int(s[i][j]))
            basin_mark[i].append(0)

    curr_basin_num = 1
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if basin_mark[i][j] == 0 and map[i][j] != 9:
                curr_basin_list = [[i, j]]
                while len(curr_basin_list) != 0:
                    basin_mark[curr_basin_list[0][0]][curr_basin_list[0][1]] = curr_basin_num
                    neighbour = []
                    if curr_basin_list[0][0] != 0:
                        neighbour.append([curr_basin_list[0][0] - 1, curr_basin_list[0][1]])
                    if curr_basin_list[0][0] != len(map) - 1:
                        neighbour.append([curr_basin_list[0][0] + 1, curr_basin_list[0][1]])
                    if curr_basin_list[0][1] != 0:
                        neighbour.append([curr_basin_list[0][0], curr_basin_list[0][1] - 1])
                    if curr_basin_list[0][1] != len(map[0]) - 1:
                        neighbour.append([curr_basin_list[0][0], curr_basin_list[0][1] + 1])

                    for n in neighbour:
                        if map[n[0]][n[1]] != 9 and basin_mark[n[0]][n[1]] == 0:
                            curr_basin_list.append(n)
                    curr_basin_list.pop(0)

                curr_basin_num += 1

    basin_count = [0, 0]
    for n in range(1, curr_basin_num + 1):
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):
                if basin_mark[i][j] == n:
                    basin_count[n] += 1
        basin_count.append(0)

    sorted_count = basin_count[:]
    sorted_count.sort()
    print(sorted_count[-1] * sorted_count[-2] * sorted_count[-3])
    return


if __name__ == '__main__':
    with open(__file__[:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

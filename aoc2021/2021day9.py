def do_part_1(s: list):
    sum_of_low_point = 0
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            up, down, left, right = 999, 999, 999, 999
            if i != 0:
                up = int(s[i - 1][j])
            if j != 0:
                left = int(s[i][j - 1])
            if i != len(s) - 1:
                down = int(s[i + 1][j])
            if j != len(s[0]) - 1:
                right = int(s[i][j + 1])

            if int(s[i][j]) < up and int(s[i][j]) < down and int(s[i][j]) < left and int(s[i][j]) < right:
                sum_of_low_point += int(s[i][j]) + 1

    print(sum_of_low_point)

    return


def do_part_2(s: list):
    map = []
    marked = []
    for i in range(0, len(s)):
        map.append([])
        marked.append([])
        for j in range(0, len(s[0])):
            map[i].append(int(s[i][j]))
            marked[i].append(0)

    basin_num = 1
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if marked[i][j] == 0 and map[i][j] != 9:
                marked[i][j] = basin_num
                neighbour = [[i, j]]
                while len(neighbour) != 0:
                    marked[neighbour[0][0]][neighbour[0][1]] = basin_num
                    if neighbour[0][0] != 0 and map[neighbour[0][0] - 1][neighbour[0][1]] != 9:
                        if marked[neighbour[0][0] - 1][neighbour[0][1]] == 0:
                            neighbour.append([neighbour[0][0] - 1, neighbour[0][1]])
                    if neighbour[0][0] != len(map) - 1 and map[neighbour[0][0] + 1][neighbour[0][1]] != 9:
                        if marked[neighbour[0][0] + 1][neighbour[0][1]] == 0:
                            neighbour.append([neighbour[0][0] + 1, neighbour[0][1]])
                    if neighbour[0][1] != 0 and map[neighbour[0][0]][neighbour[0][1] - 1] != 9:
                        if marked[neighbour[0][0]][neighbour[0][1] - 1] == 0:
                            neighbour.append([neighbour[0][0], neighbour[0][1] - 1])
                    if neighbour[0][1] != len(map[0]) - 1 and map[neighbour[0][0]][neighbour[0][1] + 1] != 9:
                        if marked[neighbour[0][0]][neighbour[0][1] + 1] == 0:
                            neighbour.append([neighbour[0][0], neighbour[0][1] + 1])
                    neighbour.pop(0)

                basin_num += 1

    basin_count = [0, 0]
    for n in range(1, basin_num + 1):
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):
                if marked[i][j] == n:
                    basin_count[n] += 1
        basin_count.append(0)

    sorted_count= basin_count[:]
    sorted_count.sort()

    print(sorted_count[-1] * sorted_count[-2] * sorted_count[-3])

    return


if __name__ == '__main__':
    with open(__file__[:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

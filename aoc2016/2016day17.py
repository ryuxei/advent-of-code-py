import hashlib


def do_part_1(s: list):
    passcode = s[0]
    route_list = [['', (0, 0)]]
    valid_route_list = []
    while len(route_list) > 0:
        curr_route = route_list[0]
        if curr_route[1] == (3, 3):
            valid_route_list.append(curr_route[:])
            route_list.pop(0)
            continue

        md5sum = hashlib.md5((passcode + curr_route[0]).encode()).hexdigest()
        up_down_left_right = [(a in 'bcdef') for a in md5sum[0:4]]
        if up_down_left_right[0] and curr_route[1][0] != 0:
            route_list.append([curr_route[0] + 'U', (curr_route[1][0] - 1, curr_route[1][1])])
        if up_down_left_right[1] and curr_route[1][0] != 3:
            route_list.append([curr_route[0] + 'D', (curr_route[1][0] + 1, curr_route[1][1])])
        if up_down_left_right[2] and curr_route[1][1] != 0:
            route_list.append([curr_route[0] + 'L', (curr_route[1][0], curr_route[1][1] - 1)])
        if up_down_left_right[3] and curr_route[1][1] != 3:
            route_list.append([curr_route[0] + 'R', (curr_route[1][0], curr_route[1][1] + 1)])

        route_list.pop(0)

    print(valid_route_list[0])
    print(len(valid_route_list[-1][0]))

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    input_str = ['rrrbmfta']

    do_part_1(input_str)
    do_part_2(input_str)

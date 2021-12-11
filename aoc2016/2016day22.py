def do_part_1(s: list):
    disk_list = normalize_input(s)  # it follows [[x, y, size, used, avail] ....]
    viable_pairs = []
    for i in range(0, len(disk_list)):
        for j in range(0, len(disk_list)):
            if disk_list[i][3] != 0:
                if i != j:
                    if disk_list[i][3] <= disk_list[j][4]:
                        viable_pairs.append([disk_list[i][0], disk_list[i][1], disk_list[j][0], disk_list[j][1]])
    print(len(viable_pairs))

    # part 2 by hand

    return


def do_part_2(s: list):
    return


def normalize_input(s) -> list:
    disk_info = []

    for entry in s:
        if '/dev/grid' in entry:
            disk = []
            disk.append(int(entry.split('-')[1][1:]))
            disk.append(int(entry.split('-')[2].split()[0][1:]))
            disk.append(int(entry.split()[1][:-1]))
            disk.append(int(entry.split()[2][:-1]))
            disk.append(int(entry.split()[3][:-1]))
            disk_info.append(disk)

    return disk_info


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

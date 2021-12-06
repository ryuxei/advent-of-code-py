def do_part_1(s: list):
    valid_triangle_count = 0
    for tri in s:
        dim = tri.split()
        a = int(dim[0])
        b = int(dim[1])
        c = int(dim[2])
        if a + b > c and a + c > b and b + c > a:
            valid_triangle_count += 1

    print('valid_triangle_count ', valid_triangle_count)
    return


def do_part_2(s: list):
    valid_count = 0
    for i in range(0, int(len(s) / 3)):
        line1 = s[3 * i].split()
        line2 = s[3 * i + 1].split()
        line3 = s[3 * i + 2].split()
        adim = [int(line1[0]), int(line2[0]), int(line3[0])]
        bdim = [int(line1[1]), int(line2[1]), int(line3[1])]
        cdim = [int(line1[2]), int(line2[2]), int(line3[2])]
        if adim[0] + adim[1] > adim[2] and adim[0] + adim[2] > adim[1] and adim[1] + adim[2] > adim[0]:
            valid_count += 1
        if bdim[0] + bdim[1] > bdim[2] and bdim[0] + bdim[2] > bdim[1] and bdim[1] + bdim[2] > bdim[0]:
            valid_count += 1
        if cdim[0] + cdim[1] > cdim[2] and cdim[0] + cdim[2] > cdim[1] and cdim[1] + cdim[2] > cdim[0]:
            valid_count += 1
    print(valid_count)
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

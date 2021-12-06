def do_part_1(s: list):
    for n in range(0, 80):
        curr_len = len(s)
        for i in range(0, curr_len):
            if s[i] == 0:
                s[i] = 6
                s.append(8)
            else:
                s[i] -= 1
    print(len(s))
    return


def do_part_2(s: list):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for feesh in s:
        num[feesh] += 1

    for n in range(0, 256):
        newborn = num.pop(0)
        num[6] += newborn
        num.append(newborn)

    print(sum(num))
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1([int(a) for a in input_str[0].split(',')])
    do_part_2([int(a) for a in input_str[0].split(',')])

    pass

def do_part_1(s: list):
    st = ''
    for i in range(0, 8):
        d = {}
        for j in range(0, len(s)):
            if s[j][i] not in d:
                d[s[j][i]] = 1
            else:
                d[s[j][i]] += 1
        st += max(d, key=d.get)
    print(st)
    return


def do_part_2(s: list):
    st = ''
    for i in range(0, 8):
        d = {}
        for j in range(0, len(s)):
            if s[j][i] not in d:
                d[s[j][i]] = 1
            else:
                d[s[j][i]] += 1
        st += min(d, key=d.get)
    print(st)
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

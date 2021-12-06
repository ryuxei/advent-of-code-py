import re


def do_part_1(s: list):
    i = 0
    length = 0
    while i < len(s[0]):
        if s[0][i] != '(':
            i += 1
            length += 1
            continue
        elif s[0][i] == '(':
            dim = [int(a) for a in s[0][i + 1:].split(')')[0].split('x')]
            i += 3 + len(str(dim[0]) + str(dim[1])) + dim[0]
            length += dim[0] * dim[1]
    print(length)
    return


def do_part_2(s: list):
    length = cal_length(s[0])
    print(length)
    return


def cal_length(s) -> int:
    length = 0
    i = 0
    while i < len(s):
        if s[i] != '(':
            i += 1
            length += 1
            continue
        elif s[i] == '(':
            right_bracket_i = s.index(')', i, len(s))
            dim = [int(a) for a in s[i + 1:right_bracket_i].split('x')]
            length += dim[1] * cal_length(s[right_bracket_i + 1:right_bracket_i + dim[0] + 1])
            i += (right_bracket_i - i + 1) + dim[0]

    return length


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

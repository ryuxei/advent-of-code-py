def do_part_1(s: list):
    register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}  # for part 1, set 'c' to 0

    i = 0
    while i < len(s):
        if 'cpy' in s[i]:
            reg = s[i][4:].split(' ')[1]
            val = s[i][4:].split(' ')[0]
            if val.isnumeric():
                register[reg] = int(val)
            else:
                register[reg] = register[val]
            i += 1
        elif 'inc' in s[i]:
            reg = s[i][-1]
            register[reg] += 1
            i += 1
        elif 'dec' in s[i]:
            reg = s[i][-1]
            register[reg] -= 1
            i += 1
        elif 'jnz' in s[i]:
            cond = s[i][4:].split(' ')[0]
            jmp_dist = int(s[i][4:].split(' ')[1])
            if cond.isnumeric() and int(cond) != 0:
                i += jmp_dist
            elif register[cond] != 0:
                i += jmp_dist
            else:
                i += 1

    print(register['a'])

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

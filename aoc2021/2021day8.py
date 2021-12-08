def do_part_1(s: list):
    count_1478 = [0, 0, 0, 0]
    val_sum = 0
    for scenario in s:
        tests = scenario.split(' | ')[0].split(' ')
        output = scenario.split(' | ')[1].split(' ')
        d = solve_wire_seg_connection(tests, gen_dict())
        nums = solve_output(output, d)
        val = int(str(nums[0]) + str(nums[1]) + str(nums[2]) + str(nums[3]))
        val_sum += val
        # part 1
        count_1478[0] += nums.count(1)
        count_1478[1] += nums.count(4)
        count_1478[2] += nums.count(7)
        count_1478[3] += nums.count(8)

    print(sum(count_1478))
    print(val_sum)

    return


def do_part_2(s: list):
    return


def gen_dict() -> dict:
    letters = 'abcdefg'
    possibility = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    d = {}
    for i in range(0, len(letters)):
        d[letters[i]] = possibility[:]
    return d


def solve_wire_seg_connection(tests, con_dict) -> dict:
    len_of_n = [[], [], [], [], [], [], [], []]
    for digit in tests:
        len_of_n[len(digit)].append(digit)

    a = len_of_n[3][0].replace(len_of_n[2][0][0], '').replace(len_of_n[2][0][1], '')
    con_dict[a] = ['a']

    c = ''
    for digit in len_of_n[6]:
        if len_of_n[2][0][0] not in digit:
            c = len_of_n[2][0][0]
            break
        elif len_of_n[2][0][1] not in digit:
            c = len_of_n[2][0][1]
            break
    con_dict[c] = ['c']

    f = len_of_n[2][0].replace(c, '')
    con_dict[f] = ['f']

    g = ''
    for digit in len_of_n[6]:
        if a in digit \
                and len_of_n[4][0][0] in digit \
                and len_of_n[4][0][1] in digit \
                and len_of_n[4][0][2] in digit \
                and len_of_n[4][0][3] in digit:
            g = digit.replace(a, '').replace(len_of_n[4][0][0], ''). \
                replace(len_of_n[4][0][1], '').replace(len_of_n[4][0][2], '').replace(len_of_n[4][0][3], '')
            break
    con_dict[g] = ['g']

    d = ''
    for digit in len_of_n[5]:
        if a in digit and c in digit and f in digit and g in digit:
            d = digit.replace(a, '').replace(c, '').replace(f, '').replace(g, '')
            break
    con_dict[d] = ['d']

    b = ''
    for digit in len_of_n[6]:
        if a in digit and c in digit and d in digit and f in digit and g in digit:
            b = digit.replace(a, '').replace(c, '').replace(d, '').replace(f, '').replace(g, '')
    con_dict[b] = ['b']

    e = len_of_n[7][0].replace(a, '').replace(b, '').replace(c, '').replace(d, '').replace(f, '').replace(g, '')
    con_dict[e] = ['e']

    return con_dict
    pass


def solve_output(output, con_dict) -> list:
    nums = []

    for o in output:
        num = ''
        for i in range(0, len(o)):
            num += con_dict[o[i]][0]
        if len(num) == 7:
            nums.append(8)
        elif len(num) == 4:
            nums.append(4)
        elif len(num) == 3:
            nums.append(7)
        elif len(num) == 2:
            nums.append(1)
        elif len(num) == 6 and 'd' not in num:
            nums.append(0)
        elif len(num) == 6 and 'c' not in num:
            nums.append(6)
        elif len(num) == 6 and 'e' not in num:
            nums.append(9)
        elif len(num) == 5 and 'f' not in num:
            nums.append(2)
        elif len(num) == 5 and 'c' not in num:
            nums.append(5)
        elif len(num) == 5 and 'c' in num and 'f' in num:
            nums.append(3)

    return nums


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

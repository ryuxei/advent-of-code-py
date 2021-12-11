def do_part_1(s: list):
    rules = []
    for raw_rule in s:
        rule = [int(a) for a in raw_rule.split('-')]
        rules.append(rule)
    rules.sort(key=left_bound)

    i = 0
    while i < len(rules) - 1:
        if rules[i][1] < rules[i + 1][0] - 1:
            i += 1
        else:
            new_rule = [rules[i][0], max(rules[i][1], rules[i + 1][1])]
            rules[i] = new_rule
            rules.pop(i + 1)
    print(rules[0][1] + 1)

    #  part 2
    valid_ip_count = 0
    for i in range(0, len(rules) - 1):
        valid_ip_count += rules[i + 1][0] - rules[i][1] - 1

    valid_ip_count += 4294967295 - rules[-1][1]
    print(valid_ip_count)

    return


def do_part_2(s: list):
    return


def left_bound(e):
    return e[0]


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

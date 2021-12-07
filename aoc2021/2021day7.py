def do_part_1(s: list):
    bounds = [min(s), max(s)]
    lowest_cost = 9999999999
    for i in range(bounds[0], bounds[1]):
        cost = 0
        for n in range(0, len(s)):
            cost += abs(s[n] - i)
        if cost < lowest_cost:
            lowest_cost = cost
    print(lowest_cost)
    return


def do_part_2(s: list):
    bounds = [min(s), max(s)]
    lowest_cost = 9999999999
    for i in range(bounds[0], bounds[1]):
        cost = 0
        for n in range(0, len(s)):
            cost += do_cost(abs(s[n] - i))
        if cost < lowest_cost:
            lowest_cost = cost
    print(lowest_cost)
    return


def do_cost(dist) -> int:
    cost = (1 + dist) * dist / 2
    return int(cost)


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1([int(a) for a in input_str[0].split(',')])
    do_part_2([int(a) for a in input_str[0].split(',')])

    pass

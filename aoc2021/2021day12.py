def do_part_1(s: list):
    m = gen_map(s)
    possible_routes = [['start']]
    small_caves = ['start', 'ez', 'mj', 'mt', 'sb', 'uw', 'vn']

    i = 0
    while i < len(possible_routes):
        print(i, len(possible_routes))
        curr_route = possible_routes[i]
        if curr_route[-1] == 'end':
            i += 1
        else:
            for new_node in m[curr_route[-1]]:
                new_route = curr_route + [new_node]
                if new_route.count('start') < 2 and new_route.count('end') < 2:
                    twice_visits = 0

                    for sm in small_caves:
                        if new_route.count(sm) == 2:
                            twice_visits += 1
                        elif new_route.count(sm) > 2:
                            twice_visits = 99
                            break

                    if twice_visits <= 1:
                        possible_routes.append(new_route)
            possible_routes.pop(i)

    return


def do_part_2(s: list):
    return


def gen_map(s) -> dict:
    m = {}
    for route in s:
        start, end = route.split('-')
        if start not in m:
            m[start] = [end]
        elif end not in m[start]:
            m[start].append(end)
        if end not in m:
            m[end] = [start]
        elif start not in m[end]:
            m[end].append(start)

    return m


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

def do_part_1(s: list):
    floors = s[:]
    length = len(floors[0])
    while len(floors) != 400000:  # 40 for part 1
        new_floor = ''
        for i in range(0, length):
            upper_left, upper_right = False, False
            if i != 0 and floors[-1][i - 1] == '^':
                upper_left = True
            if i != length - 1 and floors[-1][i + 1] == '^':
                upper_right = True
            new_floor += '^' if upper_left != upper_right else '.'
        floors.append(new_floor)

    safe_count = 0
    for floor in floors:
        safe_count += sum([(a == '.') for a in floor])
    print(safe_count)

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    input_str = ['...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^']

    do_part_1(input_str)
    do_part_2(input_str)

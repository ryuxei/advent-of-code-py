def do_part_1(s: list):
    instuctions = s[0].split(', ')
    coords = [0, 0]
    direction = [0, 1]

    for i in range(0, len(instuctions)):
        direction = rotate_direction(direction, instuctions[i][0])
        magnitude = int(instuctions[i][1:])
        coords[0] += direction[0] * magnitude
        coords[1] += direction[1] * magnitude

    print(abs(coords[0]) + abs(coords[1]))

    return


def do_part_2(s: list):
    instuctions = s[0].split(', ')
    coords = [0, 0]
    direction = [0, 1]
    visited_places = {}

    for i in range(0, len(instuctions)):
        direction = rotate_direction(direction, instuctions[i][0])
        magnitude = int(instuctions[i][1:])
        for j in range(0, magnitude):
            coords[0] += direction[0]
            coords[1] += direction[1]
            if str(coords) not in visited_places:
                visited_places[str(coords)] = 1
            else:
                print(abs(coords[0]) + abs(coords[1]))
                return

    return


def rotate_direction(curr_direction: list, rotation: str):
    direction_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    curr_index = direction_list.index(curr_direction)
    if rotation == 'L':
        return direction_list[curr_index - 1][:]
    elif rotation == 'R':
        return direction_list[(curr_index + 1) % 4][:]


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

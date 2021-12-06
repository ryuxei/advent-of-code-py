def do_part_1(s: list):
    digits = []
    curr_digit = 5
    for instruction in s:
        for i in range(0, len(instruction)):
            curr_digit = do_move(curr_digit, instruction[i])
        digits.append(curr_digit)

    print(digits)
    return


def do_part_2(s: list):
    digits = []
    curr_digit = '5'
    for instruction in s:
        for i in range(0, len(instruction)):
            curr_digit = do_new_keypad_move(curr_digit, instruction[i])
        digits.append(curr_digit)

    print(digits)
    return


def do_move(curr_key: int, direction: str) -> int:
    new_key = curr_key
    if direction == 'U':
        if curr_key not in [1, 2, 3]:
            new_key -= 3
    elif direction == 'D':
        if curr_key not in [7, 8, 9]:
            new_key += 3
    elif direction == 'L':
        if curr_key not in [1, 4, 7]:
            new_key -= 1
    elif direction == 'R':
        if curr_key not in [3, 6, 9]:
            new_key += 1
    return new_key


def do_new_keypad_move(curr_key: str, direction: str) -> str:
    new_key = curr_key
    keypad = ['0', '0', '1', '0', '0',
              '0', '2', '3', '4', '0',
              '5', '6', '7', '8', '9',
              '0', 'A', 'B', 'C', '0',
              '0', '0', 'D', '0', '0']
    if direction == 'U':
        if curr_key not in ['5', '2', '1', '4', '9']:
            new_key = keypad[keypad.index(curr_key) - 5]
    elif direction == 'D':
        if curr_key not in ['5', 'A', 'D', 'C', '9']:
            new_key = keypad[keypad.index(curr_key) + 5]
    elif direction == 'L':
        if curr_key not in ['1', '2', '5', 'A', 'D']:
            new_key = keypad[keypad.index(curr_key) - 1]
    elif direction == 'R':
        if curr_key not in ['1', '4', '9', 'C', 'D']:
            new_key = keypad[keypad.index(curr_key) + 1]
    return new_key


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

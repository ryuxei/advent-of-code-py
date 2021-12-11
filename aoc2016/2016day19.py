def do_part_1(s: list):
    # wow even i dont understand the logics in this part after finishing it
    num = int(s[0])
    state_marker, state = '', 1

    while num != 1:
        state_marker = str(state) + state_marker
        state = int((num % 2 == 0) == bool(state))
        num = num // 2 if num % 2 == 0 else (num + (2 * int(state_marker[0]))) // 2
    survivor = 1

    for i in range(0, len(state_marker)):
        survivor = 2 * survivor - int(state_marker[i])

    print(survivor)
    return


def do_part_2(s: list):
    num = int(s[0])
    crossed_off = [0 for _ in range(0, num)]

    state = 1 if num % 2 == 0 else 2
    i = num // 2
    remaining = num

    while remaining > 1:
        if state % 3 != 0:
            crossed_off[i] = 1
            remaining -= 1

        state += 1

        i = (i + 1) % num
        while crossed_off[i] != 0:
            i = (i + 1) % num

    print(crossed_off.index(0) + 1)

    return


if __name__ == '__main__':
    input_str = ['3014387']

    do_part_1(input_str)
    do_part_2(input_str)

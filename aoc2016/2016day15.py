def do_part_1(s: list):
    t = 0
    while 1:
        passed_through_stages = 0
        if (2 + t + 1) % 5 == 0:
            passed_through_stages += 1
        if (7 + t + 2) % 13 == 0:
            passed_through_stages += 1
        if (10 + t + 3) % 17 == 0:
            passed_through_stages += 1
        if (2 + t + 4) % 3 == 0:
            passed_through_stages += 1
        if (9 + t + 5) % 19 == 0:
            passed_through_stages += 1
        if (0 + t + 6) % 7 == 0:
            passed_through_stages += 1
        # part 2
        if (0 + t + 7) % 11 == 0:
            passed_through_stages += 1
        if passed_through_stages == 7:  # or 6 if it's part 1 of the problem
            print(t)
            break
        else:
            t += 1
    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

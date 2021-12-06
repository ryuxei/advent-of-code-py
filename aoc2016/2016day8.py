def do_part_1(s: list):
    screen = gen_screen()
    for ins in s:
        if 'rect' in ins:
            w = int(ins.split(' ')[1].split('x')[0])
            h = int(ins.split(' ')[1].split('x')[1])
            rect(screen, w, h)
        elif 'rotate row' in ins:
            r = int(ins.split('=')[1].split(' ')[0])
            b = int(ins.split('by ')[1])
            rotate_row(screen, r, b)
        elif 'rotate column' in ins:
            c = int(ins.split('=')[1].split(' ')[0])
            b = int(ins.split('by ')[1])
            rotate_column(screen, c, b)
    print(count_pixel(screen))
    for i in range(0, 6):
        for j in range(0, 50):
            if screen[i][j] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    return


def do_part_2(s: list):
    return


def gen_screen() -> list:
    screen = []
    for i in range(0, 6):
        screen.append([])
        for j in range(0, 50):
            screen[i].append(0)
    return screen


def rect(scr, wid, hei):
    for i in range(0, hei):
        for j in range(0, wid):
            scr[i][j] = 1


def rotate_row(scr, row, by):
    scr[row] = scr[row][50 - by:] + scr[row][:50 - by]


def count_pixel(scr) -> int:
    count = 0
    for i in range(0, 6):
        for j in range(0, 50):
            if scr[i][j] == 1:
                count += 1
    return count


def rotate_column(scr, col, by):
    column = [scr[a][col] for a in range(0, 6)]
    for i in range(0, 6):
        scr[i][col] = column[i - by]


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

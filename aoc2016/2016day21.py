def do_part_1(s: list):
    pwd = [a for a in 'abcdefgh']
    for instruction in s:
        if 'swap' in instruction:
            pos1, pos2 = 0, 0
            if 'position' in instruction:
                pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[5])
            elif 'letter' in instruction:
                pos1, pos2 = pwd.index(instruction.split(' ')[2]), pwd.index(instruction.split(' ')[5])
            pwd[pos1], pwd[pos2] = pwd[pos2], pwd[pos1]

        elif 'rotate' in instruction:
            direction = 'left' if 'left' in instruction else 'right'

            steps = 0
            if ' based on position of letter ' in instruction:
                steps = pwd.index(instruction.split(' based on position of letter ')[1])
                if steps >= 4:
                    steps += 1
                steps += 1
            elif 'step' in instruction:
                steps = int(instruction.split(' ')[2])
            steps = steps % len(pwd)

            pwd_segment = []
            if direction == 'left':
                pwd_segment = [pwd[steps:], pwd[:steps]]
            elif direction == 'right':
                pwd_segment = [pwd[len(pwd) - steps:], pwd[:len(pwd) - steps]]
            pwd = pwd_segment[0] + pwd_segment[1]

        elif 'reverse' in instruction:
            pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[4])
            pos1, pos2 = min(pos1, pos2), max(pos1, pos2)
            pwd_copy = pwd[:]
            for i in range(0, pos2 - pos1 + 1):
                pwd[pos1 + i] = pwd_copy[pos2 - i]

        elif 'move position' in instruction:
            pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[5])
            letter = pwd.pop(pos1)
            pwd.insert(pos2, letter)

    print(''.join(pwd))
    return


def do_part_2(s: list):
    pwd = [a for a in 'fbgdceah']
    for n in range(len(s) - 1, -1, -1):
        instruction = s[n]

        if 'swap' in instruction:
            pos1, pos2 = 0, 0
            if 'position' in instruction:
                pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[5])
            elif 'letter' in instruction:
                pos1, pos2 = pwd.index(instruction.split(' ')[2]), pwd.index(instruction.split(' ')[5])
            pwd[pos1], pwd[pos2] = pwd[pos2], pwd[pos1]

        elif 'rotate' in instruction:
            direction = 'right' if 'left' in instruction else 'left'

            steps = 0
            if ' based on position of letter ' in instruction:
                move_dict = [1, 1, 6, 2, 7, 3, 0, 4]
                steps = move_dict[pwd.index(instruction.split(' ')[6])]
            elif 'step' in instruction:
                steps = int(instruction.split(' ')[2])
            steps = steps % len(pwd)

            pwd_segment = []
            if direction == 'left':
                pwd_segment = [pwd[steps:], pwd[:steps]]
            elif direction == 'right':
                pwd_segment = [pwd[len(pwd) - steps:], pwd[:len(pwd) - steps]]
            pwd = pwd_segment[0] + pwd_segment[1]

        elif 'reverse' in instruction:
            pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[4])
            pos1, pos2 = min(pos1, pos2), max(pos1, pos2)
            pwd_copy = pwd[:]
            for i in range(0, pos2 - pos1 + 1):
                pwd[pos1 + i] = pwd_copy[pos2 - i]

        elif 'move position' in instruction:
            pos1, pos2 = int(instruction.split(' ')[2]), int(instruction.split(' ')[5])
            pos1, pos2 = pos2, pos1
            letter = pwd.pop(pos1)
            pwd.insert(pos2, letter)

    print(''.join(pwd))
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

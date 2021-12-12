def do_part_1(s: list):
    # NOTE:
    # set breakpoint on the three 'if's below (8, 20, and 27)
    # to see the pattern for a, b, c, and d

    a = 0
    register = {'a': 180, 'b': 0, 'c': 0, 'd': 0}  # for part 1, set 'c' to 0

    output_signal = []

    i = 0
    while i < len(s):
        curr_instruction = s[i]
        if i == 8:
            print('')
        elif i == 20:
            print('')
        elif i == 27:
            print('')
        # print(i, s[i], register, output_signal)
        if 'cpy' in curr_instruction:
            reg = curr_instruction[4:].split(' ')[1]
            val = curr_instruction[4:].split(' ')[0]
            if val.lstrip('-').isnumeric():
                register[reg] = int(val)
            else:
                register[reg] = register[val]
            i += 1
        elif 'inc' in curr_instruction:
            reg = curr_instruction[-1]
            register[reg] += 1
            i += 1
        elif 'dec' in curr_instruction:
            reg = curr_instruction[-1]
            register[reg] -= 1
            i += 1
        elif 'jnz' in curr_instruction:
            cond = curr_instruction[4:].split(' ')[0]
            jmp_dist = curr_instruction[4:].split(' ')[1]
            if cond.isnumeric() and int(cond) != 0:
                if jmp_dist.lstrip('-').isnumeric():
                    i += int(jmp_dist)
                else:
                    i += register[jmp_dist]
            elif cond.isnumeric() and int(cond) == 0:
                i += 1
            elif register[cond] != 0:
                if jmp_dist.lstrip('-').isnumeric():
                    i += int(jmp_dist)
                else:
                    i += register[jmp_dist]
            else:
                i += 1
        elif 'out' in s[i]:
            o = register[s[i].split(' ')[1]]
            if len(output_signal) == 0:
                output_signal.append(o)
                i += 1
            elif o == int(not bool(output_signal[-1])):
                output_signal.append(o)
                i += 1
                if len(output_signal) == 50:
                    print(i, s[i], register, output_signal)
                    break
            else:
                # reset
                print(i, s[i], register, output_signal)
                a += 1
                register = {'a': a, 'b': 0, 'c': 0, 'd': 0}
                output_signal = []
                i = 0
                continue
                pass

    print(register['a'])

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

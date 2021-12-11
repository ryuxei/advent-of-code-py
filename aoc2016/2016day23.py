def do_part_1(s: list):
    register = {'a': 12, 'b': 0, 'c': 0, 'd': 0}  # for part 1, set 'c' to 0

    i = 0
    while i < len(s):
        print(i, s[i], register)
        if 'cpy' in s[i]:
            reg = s[i][4:].split(' ')[1]
            val = s[i][4:].split(' ')[0]
            if val.lstrip('-').isnumeric():
                register[reg] = int(val)
            else:
                register[reg] = register[val]
            i += 1
        elif 'inc' in s[i]:
            if i == 5:
                if register['d'] > 90000 and register['b'] == register['c']:
                    register['a'] += register['b'] * register['d']
                    register['c'] -= register['c']
                    register['d'] -= register['d']
                    i += 4
                    continue

                register['a'] += register['c']
                register['c'] -= register['c']
                i += 2
                continue
            reg = s[i][-1]
            register[reg] += 1
            i += 1
        elif 'dec' in s[i]:
            reg = s[i][-1]
            register[reg] -= 1
            i += 1
        elif 'jnz' in s[i]:
            cond = s[i][4:].split(' ')[0]
            jmp_dist = s[i][4:].split(' ')[1]
            if cond.isnumeric() and int(cond) != 0:
                if jmp_dist.lstrip('-').isnumeric():
                    i += int(jmp_dist)
                else:
                    i += register[jmp_dist]
            elif register[cond] != 0:
                if jmp_dist.lstrip('-').isnumeric():
                    i += int(jmp_dist)
                else:
                    i += register[jmp_dist]
            else:
                i += 1
        elif 'tgl' in s[i]:
            offset = register[s[i].split()[1]]
            if 0 <= i + offset <= len(s) - 1:
                target_instruction = s[i + offset]
                arg_count = len(target_instruction.split(' '))
                if arg_count == 2:
                    if 'inc' in target_instruction:
                        target_instruction = target_instruction.replace('inc', 'dec')
                        s[i + offset] = target_instruction
                    else:
                        target_instruction = 'inc' + target_instruction[3:]
                        s[i + offset] = target_instruction
                elif arg_count == 3:
                    if 'jnz' in target_instruction:
                        target_instruction = target_instruction.replace('jnz', 'cpy')
                        s[i + offset] = target_instruction
                    else:
                        target_instruction = 'jnz' + target_instruction[3:]
                        s[i + offset] = target_instruction
                i += 1

            else:
                i += 1

    print(register['a'])

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

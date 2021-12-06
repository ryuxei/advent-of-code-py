def do_part_1(s: list):
    bot_inventory = {}  # it follows {'bot #': [value,...], ...}
    output_bin = {}  # it follows the same format as above

    instructions = s[:]

    i = 0
    while len(instructions) != 0:
        if 'goes to bot' in instructions[i]:
            value = int(instructions[i][6:].split(' goes to ')[0])
            bot_name = instructions[i].split(' goes to ')[1]
            if bot_name not in bot_inventory:
                bot_inventory[bot_name] = [value]
            else:
                bot_inventory[bot_name].append(value)
            instructions.pop(i)
        elif 'gives' in instructions[i]:
            bot_name = instructions[i].split(' gives ')[0]
            if bot_name not in bot_inventory or len(bot_inventory[bot_name]) != 2:
                i += 1
            else:
                # part 1 logic
                if 61 in bot_inventory[bot_name] and 17 in bot_inventory[bot_name]:
                    print('part 1: ', bot_name)
                # part 1 logic end
                low_target = instructions[i].split('gives low to ')[1].split(' and ')[0]
                high_target = instructions[i].split(' and high to ')[1]
                low_value = min(bot_inventory[bot_name][0], bot_inventory[bot_name][1])
                high_value = max(bot_inventory[bot_name][0], bot_inventory[bot_name][1])
                if 'output' in low_target:
                    output_bin[low_target] = low_value
                if 'output' in high_target:
                    output_bin[high_target] = high_value
                if 'bot' in low_target:
                    if low_target not in bot_inventory:
                        bot_inventory[low_target] = [low_value]
                    else:
                        bot_inventory[low_target].append(low_value)
                if 'bot' in high_target:
                    if high_target not in bot_inventory:
                        bot_inventory[high_target] = [high_value]
                    else:
                        bot_inventory[high_target].append(high_value)
                instructions.pop(i)

        if i >= len(instructions):
            i = 0

    # part 2 logic
    print('part 2: ', output_bin['output 0'] * output_bin['output 1'] * output_bin['output 2'])
    # part 2 logic end

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

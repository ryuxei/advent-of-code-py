def do_part_1(s: list):
    accepted_strings = []

    for pwd in s:
        letter_dict = {}
        pwd_joint = ''.join(pwd[0:-1])

        max_letter_count = 1
        for i in range(0, len(pwd_joint)):
            if pwd_joint[i] not in letter_dict:
                letter_dict[pwd_joint[i]] = 1
            else:
                letter_dict[pwd_joint[i]] += 1
                if letter_dict[pwd_joint[i]] > max_letter_count:
                    max_letter_count = letter_dict[pwd_joint[i]]

        letter_pointer = 0
        is_pwd_acceptable = 1

        for i in range(max_letter_count, 0, -1):
            if letter_pointer == 5:
                break
            if pwd[-1][1][letter_pointer] not in letter_dict:
                is_pwd_acceptable = 0
                break
            accepted_letter_list = []
            for recorded_letters in letter_dict:
                if letter_dict[recorded_letters] == i:
                    accepted_letter_list.append(recorded_letters)

            while len(accepted_letter_list) > 0 and letter_pointer != 5:
                if pwd[-1][1][letter_pointer] in accepted_letter_list:
                    accepted_letter_list.pop(accepted_letter_list.index(pwd[-1][1][letter_pointer]))
                    letter_pointer += 1
                else:
                    is_pwd_acceptable = 0
                    break

            if not is_pwd_acceptable:
                break

        if is_pwd_acceptable:
            accepted_strings.append(pwd[:])

    sum = 0

    for accepted_string in accepted_strings:
        sum += accepted_string[-1][0]

    print(sum)

    decoded_strings = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for string in accepted_strings:
        decoded = ''
        concat_str = '-'.join(string[:-1])
        for i in range(0, len(concat_str)):
            if concat_str[i] == '-':
                decoded += ' '
                continue
            else:
                decoded += alphabets[(alphabets.index(concat_str[i]) + string[-1][0]) % len(alphabets)]
        decoded_strings.append(decoded)
        if 'north' in decoded:
            print(string)

    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    parsed_input = []
    for i in range(0, len(input_str)):
        parsed_input.append(input_str[i].split('-'))
        parsed_input[i][-1] = parsed_input[i][-1].split('[')
        parsed_input[i][-1][0] = int(parsed_input[i][-1][0])
        parsed_input[i][-1][1] = parsed_input[i][-1][1][:-1]

    do_part_1(parsed_input)
    do_part_2(input_str)

    pass

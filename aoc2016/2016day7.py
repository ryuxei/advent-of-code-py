import re


def do_part_1(s: list):
    acceptable_count = 0
    for addr in s:
        is_acceptable = False
        out_hypernet_seq = re.split(r'\[.*?]', addr)
        in_hypernet_seq = re.findall(r'\[.*?]', addr)
        for out_seq in out_hypernet_seq:
            for i in range(0, len(out_seq) - 3):
                if out_seq[i] == out_seq[i + 3] and out_seq[i + 1] == out_seq[i + 2] and out_seq[i] != out_seq[i + 1]:
                    is_acceptable = True
        for in_seq in in_hypernet_seq:
            for i in range(0, len(in_seq) - 3):
                if in_seq[i] == in_seq[i + 3] and in_seq[i + 1] == in_seq[i + 2] and in_seq[i] != in_seq[i + 1]:
                    is_acceptable = False
        if is_acceptable:
            acceptable_count += 1
    print('acceptable_count ', acceptable_count)
    return


def do_part_2(s: list):
    acceptable_count = 0
    for addr in s:
        letters = []
        is_acceptable = 0
        out_hypernet_seq = re.split(r'\[.*?]', addr)
        in_hypernet_seq = re.findall(r'\[.*?]', addr)
        for out_seq in out_hypernet_seq:
            for i in range(0, len(out_seq) - 2):
                if out_seq[i] == out_seq[i + 2] and out_seq[i] != out_seq[i + 1]:
                    is_acceptable = 1
                    letters.append([out_seq[i], out_seq[i + 1]])
        for in_seq in in_hypernet_seq:
            for i in range(0, len(in_seq) - 2):
                if in_seq[i] == in_seq[i + 2] and in_seq[i] != in_seq[i + 1]:
                    for lett in letters:
                        if in_seq[i] == lett[1] and in_seq[i + 1] == lett[0]:
                            is_acceptable = 2
        if is_acceptable == 2:
            acceptable_count += 1
    print('acceptable_count ', acceptable_count)
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

    pass

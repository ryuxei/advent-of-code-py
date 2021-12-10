def do_part_1(s: list):
    rand_data = gen_dragon_thing(s[0], 272)[0:272]
    checksum = gen_checksum(rand_data)
    print(checksum)
    return


def do_part_2(s: list):
    rand_data = gen_dragon_thing(s[0], 35651584)[0:35651584]
    checksum = gen_checksum(rand_data)
    print(checksum)
    return


def gen_dragon_thing(s, length) -> str:
    rev = s[::-1].replace('1', 'A').replace('0', '1').replace('A', '0')
    new_s = s + '0' + rev
    if len(new_s) >= length:
        return new_s
    else:
        return gen_dragon_thing(new_s, length)


def gen_checksum(s) -> str:
    if len(s) % 2 == 1:
        return s
    else:
        checksum = ''
        for i in range(0, len(s)):
            if i % 2 == 0:
                checksum += '1' if s[i] == s[i + 1] else '0'
        return gen_checksum(checksum)


if __name__ == '__main__':
    input_str = ['10001001100000001']

    do_part_1(input_str)
    do_part_2(input_str)

curr_pass = 'vzbxxyzz'


def get_next_letter(lett: str) -> str:
    letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                   'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                   'x': 23, 'y': 24, 'z': 25, }
    letters = 'abcdefghijklmnopqrstuvwxyz'

    if lett == 'z':
        return ''
    else:
        return letters[letter_dict[lett] + 1]


def check_if_valid(pwd: str) -> bool:
    is_three_straight = 0
    is_forbidden_letters = 0
    is_pairs = []

    for i in range(0, len(pwd)):
        if i < len(pwd) - 2 \
                and pwd[i + 1] == get_next_letter(pwd[i]) \
                and pwd[i + 2] == get_next_letter(get_next_letter(pwd[i])):
            is_three_straight = 1
        if pwd[i] == 'i' or pwd[i] == 'o' or pwd[i] == 'l':
            is_forbidden_letters = 1
        if i < len(pwd) - 1:
            if pwd[i] == pwd[i + 1] and i - 1 not in is_pairs:
                is_pairs.append(i)
        pass

    if is_three_straight == 1 and is_forbidden_letters == 0 and len(is_pairs) >= 2:
        return True
    else:
        return False


def get_next_pass(curr: str) -> str:
    if curr == 'zzzzzzzz':
        return ''

    new_pass = []
    for i in range(0, len(curr)):
        new_pass.append(curr[i])

    carry_one = 0

    if new_pass[-1] == 'z':
        carry_one = 1
        for i in range(len(new_pass) - 1, 0 - 1, -1):
            if carry_one == 0:
                break
            elif carry_one == 1:
                if new_pass[i] == 'z':
                    new_pass[i] = 'a'
                    carry_one = 1
                else:
                    new_pass[i] = get_next_letter(new_pass[i])
                    carry_one = 0
    else:
        new_pass[-1] = get_next_letter(new_pass[-1])

    new_pass_str = ''
    for i in range(0, len(new_pass)):
        new_pass_str += new_pass[i]

    return new_pass_str


while curr_pass != 'zzzzzzzz':
    curr_pass = get_next_pass(curr_pass)
    if check_if_valid(curr_pass):
        break

print(curr_pass)

def do_part_1(s: list):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ses_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    syntax_error_score = 0
    incomplete_score_list = []
    incomplete_score_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    for line in s:
        left_brackets = []
        is_erroneous = False
        for bracket in line:
            if bracket in pairs:
                left_brackets.append(bracket)
            elif len(left_brackets) != 0 and bracket == pairs[left_brackets[-1]]:
                left_brackets.pop(-1)
            else:
                syntax_error_score += ses_dict[bracket]
                is_erroneous = True
                break
        # part 2
        if not is_erroneous:
            incomplete_score = 0
            for i in range(len(left_brackets) - 1, -1, -1):
                incomplete_score *= 5
                incomplete_score += incomplete_score_dict[pairs[left_brackets[i]]]
            incomplete_score_list.append(incomplete_score)
    print(syntax_error_score)
    incomplete_score_list.sort()
    print(incomplete_score_list[len(incomplete_score_list) // 2])
    return


def do_part_2(s: list):
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1(input_str)
    do_part_2(input_str)

# 2015 day 5
f = open('santa1.txt', 'r')
strings = f.read().splitlines()
f.close()

letters = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  # corresponds to [a, e, i, o, u]
previous_letter = ''
is_twice_in_a_row = 0  # does it satisfy the 'twice-in-a-row' requirement yet?
is_forbidden_combo = 0  # does it contain 'ab', 'cd', 'pq', or 'xy'?

vowel_count = 0
nice_word_count = 0

for line in strings:

    letters = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    previous_letter = ''
    is_twice_in_a_row = 0
    is_forbidden_combo = 0
    vowel_count = 0

    for i in range(0, len(line)):
        if line[i] not in letters:
            letters[line[i]] = 1
        else:
            letters[line[i]] += 1

        if previous_letter != '':
            if line[i] == previous_letter:
                is_twice_in_a_row = 1
            if previous_letter == 'a' and line[i] == 'b':
                is_forbidden_combo = 1
            if previous_letter == 'c' and line[i] == 'd':
                is_forbidden_combo = 1
            if previous_letter == 'p' and line[i] == 'q':
                is_forbidden_combo = 1
            if previous_letter == 'x' and line[i] == 'y':
                is_forbidden_combo = 1
        previous_letter = line[i]

    vowel_count = letters['a'] + letters['e'] + letters['i'] + letters['o'] + letters['u']

    if vowel_count >= 3 and is_twice_in_a_row == 1 and is_forbidden_combo == 0:
        nice_word_count += 1

    print(line, vowel_count, is_twice_in_a_row, is_forbidden_combo, nice_word_count)

print(nice_word_count)

print('finished')

f = open('santa1.txt', 'r')
strings = f.read().splitlines()
f.close()

is_pair_twiced = 0
is_repeating_letter = 0
nice_word_count = 0

pair_dict = {}

for line in strings:
    is_pair_twiced = 0
    is_repeating_letter = 0
    pair_dict = {}

    for i in range(0, len(line)):
        if i > 0:
            pair = line[i - 1] + line[i]
            if pair not in pair_dict:
                pair_dict[pair] = 1
            else:
                if line[i - 1] == line[i]:
                    if i > 1 and line[i - 2] == line[i]:
                        if i == 2:
                            pair_dict[pair] = 0
                        elif i > 2 and line[i - 3] != line[i]:
                            pair_dict[pair] = 0
                pair_dict[pair] += 1
                if pair_dict[pair] == 2:
                    is_pair_twiced = 1
                    print(pair)

        if i > 1 and line[i - 2] == line[i]:
            is_repeating_letter = 1

    if is_pair_twiced == 1 and is_repeating_letter == 1:
        nice_word_count += 1

    print(line, is_pair_twiced, is_repeating_letter, nice_word_count)

print(nice_word_count)

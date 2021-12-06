f = open('2015day8.txt', 'r')
strings = f.read()
f.close()

import re

part_1_string = strings[:]
part_1_string = part_1_string.replace('\n', '')
a = len(part_1_string)

part_1_string = part_1_string.replace('\\\\', 'C')
part_1_string = part_1_string.replace('\\\"', 'B')
part_1_string = re.sub('\\\\x..', 'A', part_1_string)
part_1_string = part_1_string.replace('"', '')
b = len(part_1_string)

print(a - b)

part_2_string = strings[:].splitlines()

char_count_diff = 0

for i in range(0, len(part_2_string)):
    char_count_diff += 4
    char_count_diff += part_2_string[i].count('\\\\') * 2
    part_2_string[i] = part_2_string[i].replace('\\\\', 'C')
    char_count_diff += part_2_string[i].count('\\\"') * 2
    part_2_string[i] = part_2_string[i].replace('\\\"', 'B')
    char_count_diff += part_2_string[i].count('\\x')
    pass

print(char_count_diff)
pass

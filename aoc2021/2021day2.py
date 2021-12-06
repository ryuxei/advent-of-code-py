f = open('2021day2.txt', 'r')
strings = f.read().splitlines()
f.close()

depth = 0
hori_length = 0

for i in range(0, len(strings)):
    if 'forward' in strings[i]:
        hori_length += int(strings[i].split(' ')[1])
    elif 'down' in strings[i]:
        depth += int(strings[i].split(' ')[1])
    elif 'up' in strings[i]:
        depth -= int(strings[i].split(' ')[1])

print(depth * hori_length)

depth = 0
hori_length = 0
aim = 0

for i in range(0, len(strings)):
    if 'forward' in strings[i]:
        hori_length += int(strings[i].split(' ')[1])
        depth += aim * int(strings[i].split(' ')[1])
    elif 'down' in strings[i]:
        aim += int(strings[i].split(' ')[1])
    elif 'up' in strings[i]:
        aim -= int(strings[i].split(' ')[1])

print(depth * hori_length)
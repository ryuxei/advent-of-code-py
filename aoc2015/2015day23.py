f = open('2015day23.txt', 'r')
strings = f.read().splitlines()
f.close()

register = {'a': 1, 'b': 0}

i = 0

# !!! UNSIGNED INT

while 0 <= i < len(strings):
    if 'hlf' in strings[i]:
        register[strings[i][4:5]] = int(register[strings[i][4:5]] / 2)
    if 'tpl' in strings[i]:
        register[strings[i][4:5]] *= 3
    elif 'inc' in strings[i]:
        register[strings[i][4:5]] += 1
    elif 'jmp' in strings[i]:
        i += int(strings[i].split(' ')[1])
        continue
    elif 'jie' in strings[i]:
        if register[strings[i][4:5]] % 2 == 0:
            i += int(strings[i].split(', ')[1])
            continue
    elif 'jio' in strings[i]:
        if register[strings[i][4:5]] == 1:
            i += int(strings[i].split(', ')[1])
            continue
    i += 1

print(register)

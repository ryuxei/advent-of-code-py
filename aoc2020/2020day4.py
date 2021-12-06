f = open('2020day4.txt', 'r')
strings = f.read().split('\n\n')
f.close()

#  part 1
valid_count = 0
for passport in strings:
    criteria = 0
    if 'byr' in passport:
        criteria += 1
    if 'iyr' in passport:
        criteria += 1
    if 'eyr' in passport:
        criteria += 1
    if 'hgt' in passport:
        criteria += 1
    if 'hcl' in passport:
        criteria += 1
    if 'ecl' in passport:
        criteria += 1
    if 'pid' in passport:
        criteria += 1
    if criteria >= 7:
        valid_count += 1

print(valid_count)

#  part 2
new_valid_count = 0

for i in range(0, len(strings)):
    normalized = strings[i].replace('\n', ' ').split(' ')
    strings[i] = normalized

for passport in strings:
    criteria = 0
    for entry in passport:
        if 'byr' in entry:
            if len(entry[4:]) == 4 and int(entry[4:]) in range(1920, 2002 + 1):
                criteria += 1
        if 'iyr' in entry:
            if len(entry[4:]) == 4 and int(entry[4:]) in range(2010, 2020 + 1):
                criteria += 1
        if 'eyr' in entry:
            if len(entry[4:]) == 4 and int(entry[4:]) in range(2020, 2030 + 1):
                criteria += 1
        if 'hgt' in entry:
            if entry[-2:] == 'cm' and int(entry[4:-2]) in range(150, 193 + 1):
                criteria += 1
            elif entry[-2:] == 'in' and int(entry[4:-2]) in range(59, 76 + 1):
                criteria += 1
        if 'hcl' in entry:
            if len(entry[4:]) == 7:
                if entry[4] == '#':
                    if entry[5] in '0123456789abcdefABCDEF':
                        if entry[6] in '0123456789abcdefABCDEF':
                            if entry[7] in '0123456789abcdefABCDEF':
                                if entry[8] in '0123456789abcdefABCDEF':
                                    if entry[9] in '0123456789abcdefABCDEF':
                                        if entry[10] in '0123456789abcdefABCDEF':
                                            criteria += 1
        if 'ecl' in entry:
            if entry[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                criteria += 1
        if 'pid' in entry:
            if len(entry[4:]) == 9:
                n = 0
                for num in entry[4:]:
                    if num in '0123456789':
                        n += 1
                if n == 9:
                    criteria += 1

    if criteria >= 7:
        new_valid_count += 1

print(new_valid_count)

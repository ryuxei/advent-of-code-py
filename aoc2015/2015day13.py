f = open('2015day13.txt', 'r')
strings = f.read().splitlines()
f.close()


def gen_perm() -> list:
    perm_list = []
    perm = [-1, -1, -1, -1, -1, -1, -1, -1]
    for i in range(0, 8):
        perm[0] = i
        for j in range(0, 8):
            if j in perm and perm[1] != j:
                continue
            else:
                perm[1] = j
            for k in range(0, 8):
                if k in perm and perm[2] != k:
                    continue
                else:
                    perm[2] = k
                for l in range(0, 8):
                    if l in perm and perm[3] != l:
                        continue
                    else:
                        perm[3] = l
                    for m in range(0, 8):
                        if m in perm and perm[4] != m:
                            continue
                        else:
                            perm[4] = m
                        for n in range(0, 8):
                            if n in perm and perm[5] != n:
                                continue
                            else:
                                perm[5] = n
                            for o in range(0, 8):
                                if o in perm and perm[6] != o:
                                    continue
                                else:
                                    perm[6] = o
                                for p in range(0, 8):
                                    if p in perm:
                                        continue
                                    else:
                                        perm[7] = p
                                        perm_list.append(perm[:])
                                        perm[7] = -1
                                        break
                                perm[6] = -1
                            perm[5] = -1
                        perm[4] = -1
                    perm[3] = -1
                perm[2] = -1
            perm[1] = -1
        perm[0] = -1
    return perm_list


def gen_happiness_dict(rules: list) -> dict:
    happ_dict = {}
    for i in range(0, len(rules)):
        entry = []
        entry.append(rules[i].split(' ')[0])
        entry.append(rules[i].split(' ')[-1][:-1])
        entry.append(int(rules[i].split(' ')[3]))
        if 'lose' in rules[i]:
            entry[2] = -entry[2]
        if entry[0] not in happ_dict:
            happ_dict[entry[0]] = {}
        happ_dict[entry[0]][entry[1]] = entry[2]
    return happ_dict


people_list = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']
seating_perms = gen_perm()
happiness_dict = gen_happiness_dict(strings)

best_happiness_level = 0
best_happiness_settings = []

for i in range(0, len(seating_perms)):
    curr_happiness_level = 0
    for j in range(0, len(seating_perms[i])):
        if j < 7:
            curr_happiness_level += happiness_dict[people_list[seating_perms[i][j]]][
                people_list[seating_perms[i][(j + 1) % 8]]]
        if j > 0:
            curr_happiness_level += happiness_dict[people_list[seating_perms[i][j]]][
                people_list[seating_perms[i][(j - 1) % 8]]]
    if curr_happiness_level > best_happiness_level:
        best_happiness_settings = seating_perms[i][:]
        best_happiness_level = curr_happiness_level

pass

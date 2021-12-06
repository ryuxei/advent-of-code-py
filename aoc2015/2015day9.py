f = open('2015day9.txt', 'r')
strings = f.read().splitlines()
f.close()


# input [1, 2, 4, 5, 3] -> return [1, 2, 5, 3, 4]
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


def gen_distance(strings: list) -> dict:
    dis_dict = {}
    for i in range(0, len(strings)):
        entry = []
        entry.append(strings[i].split(' to ')[0])
        entry.append(strings[i].split(' to ')[1].split(' = ')[0])
        entry.append(strings[i].split(' to ')[1].split(' = ')[1])
        if entry[0] not in dis_dict:
            dis_dict[entry[0]] = {}
        if entry[1] not in dis_dict:
            dis_dict[entry[1]] = {}
        dis_dict[entry[0]][entry[1]] = int(entry[2])
        dis_dict[entry[1]][entry[0]] = int(entry[2])
    return dis_dict


# def get_distance()
loc = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
dis_dict = gen_distance(strings)
route_list = gen_perm()

min_dist = 999999
min_route = []

for i in range(0, len(route_list)):
    curr_dist = 0
    for j in range(0, len(route_list[i]) - 1):
        curr_dist += dis_dict[loc[route_list[i][j]]][loc[route_list[i][j + 1]]]
    if curr_dist < min_dist:
        min_dist = curr_dist
        min_route = route_list[i][:]

print(min_dist, min_route)
pass

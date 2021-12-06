f = open('2015day14.txt', 'r')
strings = f.read().splitlines()
f.close()


def get_reindeer_stats(stats: list) -> list:
    s = []
    for i in range(0, len(stats)):
        entry = []
        e = stats[i].split(' ')
        entry.append(e[0])
        entry.append(int(e[3]))
        entry.append(int(e[6]))
        entry.append(int(e[13]))
        s.append(entry)
    return s


def get_total_distance_at_time(sec: int, stats: list) -> int:
    completed_cycles = int(sec / (stats[2] + stats[3]))
    remainder_time = sec % (stats[2] + stats[3])
    total_travelled = (completed_cycles * stats[2] + min(remainder_time, stats[2])) * stats[1]
    return total_travelled


reindeer_stats = get_reindeer_stats(strings)

for i in range(0, len(reindeer_stats)):
    print(reindeer_stats[i][0], get_total_distance_at_time(2503, reindeer_stats[i]))

print('--------')

scoreboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 2504):
    best_distance = 0
    best_reindeer_index = []
    for j in range(0, len(reindeer_stats)):
        distance = get_total_distance_at_time(i, reindeer_stats[j])
        if distance > best_distance:
            best_distance = distance
            best_reindeer_index = [j]
        elif distance == best_distance:
            best_reindeer_index.append(j)
    for k in range(0, len(best_reindeer_index)):
        scoreboard[best_reindeer_index[k]] += 1

print(scoreboard)

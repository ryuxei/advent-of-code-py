f = open('2020day3.txt', 'r')
strings = f.read().splitlines()
f.close()

#  part 1
tree_count = 0

for i in range(0, len(strings)):
    if strings[i][(i * 3) % len(strings[0])] == '#':
        tree_count += 1

print(tree_count)

#  part 2
t_count = [0, 0, 0, 0, 0]
t_count[1] = tree_count

for i in range(0, len(strings)):
    if strings[i][(i * 1) % len(strings[0])] == '#':
        t_count[0] += 1

for i in range(0, len(strings)):
    if strings[i][(i * 5) % len(strings[0])] == '#':
        t_count[2] += 1

for i in range(0, len(strings)):
    if strings[i][(i * 7) % len(strings[0])] == '#':
        t_count[3] += 1

for i in range(0, int(len(strings) / 2)+1):
    x = (i * 1) % len(strings[0])
    y = i * 2
    if strings[y][x] == '#':
        t_count[4] += 1

print(t_count[0],
      t_count[1],
      t_count[2],
      t_count[3],
      t_count[4],
      t_count[0] * t_count[1] * t_count[2] * t_count[3] * t_count[4])

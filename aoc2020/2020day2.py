f = open('2020day2.txt', 'r')
strings = f.read().splitlines()
f.close()

processed_sets = []

for line in strings:
    x = line.split(' ')
    lim = x[0].split('-')
    x[0] = [int(lim[0]), int(lim[1])]
    x[1] = x[1][0]
    processed_sets.append(x)

#  part 1
valid_count = 0

for entry in processed_sets:
    if entry[2].count(entry[1]) in range(entry[0][0], entry[0][1] + 1):
        valid_count += 1
    pass

print(valid_count)

#  part 2
new_valid_count = 0

for entry in processed_sets:
    is_contain = 0
    if entry[2][entry[0][0] - 1] == entry[1]:
        is_contain += 1
    if entry[2][entry[0][1] - 1] == entry[1]:
        is_contain += 1
    if is_contain == 1:
        new_valid_count += 1

print(new_valid_count)

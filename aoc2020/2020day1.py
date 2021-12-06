f = open('2020day1.txt', 'r')
strings = f.read().splitlines()
f.close()

#  part 1
for a in range(0, len(strings) - 1):
    for b in range(a + 1, len(strings)):
        if int(strings[a]) + int(strings[b]) == 2020:
            print(strings[a], strings[b], int(strings[a]) * int(strings[b]))

#  part 2
for a in range(0, len(strings) - 2):
    for b in range(a + 1, len(strings) - 1):
        for c in range(b + 1, len(strings)):
            if int(strings[a]) + int(strings[b]) + int(strings[c]) == 2020:
                print(strings[a], strings[b], strings[c], int(strings[a]) * int(strings[b]) * int(strings[c]))

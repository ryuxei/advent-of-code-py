f = open('2021day1.txt', 'r')
strings = f.read().splitlines()
f.close()

counter = 0

for i in range(1, len(strings)):
    if int(strings[i]) > int(strings[i - 1]):
        counter += 1

print(counter)

counter = 0

for i in range(3, len(strings)):
    a = int(strings[i - 3]) + int(strings[i - 2]) + int(strings[i - 1])
    b = int(strings[i - 2]) + int(strings[i - 1]) + int(strings[i])
    if b > a:
        counter += 1

print(counter)

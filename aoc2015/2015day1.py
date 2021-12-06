f = open('2015day1.txt', 'r')
strings = f.read().splitlines()
f.close()

floor_num = 0
for i in range(0, len(strings[0])):
    if strings[0][i] == '(':
        floor_num += 1
    else:
        floor_num -= 1

print(floor_num)

# part 2
floor_num = 0
for i in range(0, len(strings[0])):
    if strings[0][i] == '(':
        floor_num += 1
    else:
        floor_num -= 1
    if floor_num == -1:
        print(i + 1)
        break

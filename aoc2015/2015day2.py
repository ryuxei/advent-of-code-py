f = open('2015day2.txt', 'r')
strings = f.read().splitlines()
f.close()

dim = []
for i in range(0, len(strings)):
    x = strings[i].split('x')
    dim.append([int(x[0]), int(x[1]), int(x[2])])

sq_footage = 0
for i in range(0, len(dim)):
    side_a = dim[i][0] * dim[i][1]
    side_b = dim[i][1] * dim[i][2]
    side_c = dim[i][0] * dim[i][2]
    sq_footage += 2 * (side_a + side_b + side_c) + min(side_a, side_b, side_c)

print(sq_footage)

ribbon_len = 0
for i in range(0, len(dim)):
    longest_side = max(dim[i][0], dim[i][1], dim[i][2])
    ribbon_len += 2 * (dim[i][0] + dim[i][1] + dim[i][2] - longest_side) + dim[i][0] * dim[i][1] * dim[i][2]

print(ribbon_len)
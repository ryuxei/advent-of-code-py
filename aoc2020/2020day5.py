f = open('2020day5.txt', 'r')
strings = f.read().splitlines()
f.close()


def decode_seat(seat: str) -> [int, int]:
    row = int(seat[0:7].replace('F', '0').replace('B', '1'), base=2)
    column = int(seat[7:10].replace('L', '0').replace('R', '1'), base=2)
    return [row, column]


def seat_to_id(seat: [int, int]) -> int:
    return seat[0] * 8 + seat[1]


def print_seat_map(map):
    for i in range(0, len(map)):
        print('%.3d' % (i), end=' ')
        for j in range(0, len(map[i])):
            print(map[i][j], end='')
        print('\n', end='')


#  part 1
highest_id = 0
for i in range(0, len(strings)):
    curr_id = seat_to_id(decode_seat(strings[i]))
    if curr_id > highest_id:
        highest_id = curr_id

print("highest id: " + str(highest_id))

#  part 2
seat_map = []
for i in range(0, 128):
    seat_map.append([])
    for j in range(0, 8):
        seat_map[i].append('.')

for i in range(0, len(strings)):
    seat = decode_seat(strings[i])
    seat_map[seat[0]][seat[1]] = '#'

print_seat_map(seat_map)
print(seat_to_id([80,2]))

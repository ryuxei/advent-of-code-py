f = open('2015day7.txt', 'r')
strings = f.read().splitlines()
f.close()

# available operations: AND, OR, LSHIFT, RSHIFT, NOT, *EQUAL
instructions = []

# normalizing data
for i in range(0, len(strings)):
    entry = []
    entry.append(strings[i].split(' -> ')[1])
    if 'AND' in strings[i]:
        entry.append('AND')
        entry.append(strings[i].split(' AND ')[0])
        entry.append(strings[i].split(' AND ')[1].split(' -> ')[0])
    elif 'OR' in strings[i]:
        entry.append('OR')
        entry.append(strings[i].split(' OR ')[0])
        entry.append(strings[i].split(' OR ')[1].split(' -> ')[0])
    elif 'LSHIFT' in strings[i]:
        entry.append('LSHIFT')
        entry.append(strings[i].split(' LSHIFT ')[0])
        entry.append(int(strings[i].split(' LSHIFT ')[1].split(' -> ')[0]))
    elif 'RSHIFT' in strings[i]:
        entry.append('RSHIFT')
        entry.append(strings[i].split(' RSHIFT ')[0])
        entry.append(int(strings[i].split(' RSHIFT ')[1].split(' -> ')[0]))
    elif 'NOT' in strings[i]:
        entry.append('NOT')
        entry.append(strings[i].split(' -> ')[0][4:])
    elif ' -> ' in strings[i]:
        entry.append('EQUAL')
        entry.append(strings[i].split(' -> ')[0])
    instructions.append(entry)

del strings, i, f, entry

# main parser
wire_dict = {}
for i in range(0, len(instructions)):
    for j in range(0, len(instructions)):
        if instructions[j][0] not in wire_dict:
            if instructions[j][1] == 'EQUAL':
                if instructions[j][2].isnumeric():
                    wire_dict[instructions[j][0]] = int(instructions[j][2])
                elif instructions[j][2] in wire_dict:
                    wire_dict[instructions[j][0]] = wire_dict[instructions[j][2]]
            elif instructions[j][1] == 'AND':
                if instructions[j][2] in wire_dict or instructions[j][2].isnumeric():
                    if instructions[j][3] in wire_dict or instructions[j][3].isnumeric():
                        if instructions[j][2].isnumeric():
                            left = int(instructions[j][2])
                        else:
                            left = wire_dict[instructions[j][2]]
                        if instructions[j][3].isnumeric():
                            right = int(instructions[j][3])
                        else:
                            right = wire_dict[instructions[j][3]]
                        wire_dict[instructions[j][0]] = left & right
            elif instructions[j][1] == 'OR':
                if instructions[j][2] in wire_dict or instructions[j][2].isnumeric():
                    if instructions[j][3] in wire_dict or instructions[j][3].isnumeric():
                        if instructions[j][2].isnumeric():
                            left = int(instructions[j][2])
                        else:
                            left = wire_dict[instructions[j][2]]
                        if instructions[j][3].isnumeric():
                            right = int(instructions[j][3])
                        else:
                            right = wire_dict[instructions[j][3]]
                        wire_dict[instructions[j][0]] = left | right
            elif instructions[j][1] == 'LSHIFT':
                if instructions[j][2] in wire_dict:
                    wire_dict[instructions[j][0]] = (wire_dict[instructions[j][2]] << instructions[j][3]) & 65535
            elif instructions[j][1] == 'RSHIFT':
                if instructions[j][2] in wire_dict:
                    wire_dict[instructions[j][0]] = (wire_dict[instructions[j][2]] >> instructions[j][3]) & 65535
            elif instructions[j][1] == 'NOT':
                if instructions[j][2] in wire_dict:
                    wire_dict[instructions[j][0]] = (~wire_dict[instructions[j][2]]) & 65535

print(wire_dict['a'])
pass

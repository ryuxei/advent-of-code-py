f = open('2020day8.txt', 'r')
strings = f.read().splitlines()
f.close()


def get_offset(rule: str) -> int:
    sign = 1
    if rule[4] == '-':
        sign = -1
    return sign * int(rule[5:])


def main_run(instructions) -> []:
    accumulator = 0
    execution_history = []
    i = 0
    finished = 1
    while i < len(instructions):
        instruction = instructions[i]
        if i in execution_history:
            finished = 0
            break
        execution_history.append(i)
        if instruction[0:3] == 'nop':
            i += 1
        elif instruction[0:3] == 'acc':
            accumulator += get_offset(instruction)
            i += 1
        elif instruction[0:3] == 'jmp':
            i += get_offset(instruction)

    return [accumulator, execution_history, finished]


for i in range(0, len(strings)):
    if strings[i][0:3] == 'nop':
        instructions_modified = strings[:]
        instructions_modified[i] = instructions_modified[i].replace('nop', 'jmp')
        results = main_run(instructions_modified)
    elif strings[i][0:3] == 'jmp':
        instructions_modified = strings[:]
        instructions_modified[i] = instructions_modified[i].replace('jmp', 'nop')
        results = main_run(instructions_modified)
    else:
        continue
    if results[2] == 1:
        print(results[0])
        print(results[1])

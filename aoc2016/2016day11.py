# this implementation is very messy and inefficient.

def do_part_1():
    state = gen_initial_state()
    moves = [[a] for a in gen_valid_moves(state, gen_possible_moves(state))]

    unique_states = {}
    unique_states_moves = {}

    state_str = gen_state(state)
    unique_states[state_str] = 0

    while 1:
        state = gen_initial_state()
        for move in moves[0]:
            do_move(state, move)
        if is_finished(state):
            print('answer: ', len(moves[0]), moves[0])
            break
        else:
            state_str = gen_state(state)
            if state_str in unique_states and len(moves[0]) >= unique_states[state_str]:
                moves.remove(moves[0])
                continue
            unique_states[state_str] = len(moves[0])
            unique_states_moves[state_str] = moves[0]
            valid_moves = gen_valid_moves(state, gen_possible_moves(state))
            last_move_reverse = [moves[0][-1][0], 'up' if moves[0][-1][1] == 'down' else 'down']
            # curr_move = moves[0][:]
            for valid_move in valid_moves:
                if valid_move != last_move_reverse:
                    moves.append(moves[0] + [valid_move])
            moves.remove(moves[0])
        print(len(moves), moves[0])
    return


def do_part_2(s: list):
    return


def gen_initial_state() -> list:
    f4 = []
    f3 = ['COC', 'CUC', 'RUC', 'PLC']
    f2 = ['COG', 'CUG', 'RUG', 'PLG']
    f1 = ['PRG', 'PRC', 'ELG', 'ELC', 'DIG', 'DIC']  # this is specific to part 2
    elevator_pos = 1
    return [elevator_pos, f1, f2, f3, f4]


def is_there_generators(floor) -> bool:
    for item in floor:
        if item[2] == 'G':
            return True


def gen_possible_moves(state) -> list:
    possible_moves = []
    possible_inventory = []
    possible_directions = []
    if 1 <= state[0] <= 3:
        possible_directions.append('up')
    if 2 <= state[0] <= 4:
        possible_directions.append('down')

    for item in state[state[0]]:
        possible_inventory.append([item])
    for i in range(0, len(state[state[0]]) - 1):
        for j in range(i + 1, len(state[state[0]])):
            possible_inventory.append([state[state[0]][i], state[state[0]][j]])

    for direction in possible_directions:
        for inventory in possible_inventory:
            possible_moves.append([inventory, direction])

    return possible_moves


def gen_valid_moves(state, possible_moves) -> list:
    valid_moves = []

    for move in possible_moves:
        is_move_valid = True

        # check leaving-floor is okay
        leaving_floor = state[state[0]][:]
        for item in move[0]:
            leaving_floor.remove(item)
        for item in leaving_floor:
            if is_there_generators(leaving_floor) and (item[2] == 'C') and (item[0:2] + 'G' not in leaving_floor):
                is_move_valid = False
                break

        # check arriving-floor will be okay
        elevator_movement = 1 if move[1] == 'up' else -1
        arriving_floor = state[state[0] + elevator_movement][:]
        for item in move[0]:
            arriving_floor.append(item)
        for item in arriving_floor:
            if is_there_generators(arriving_floor) and (item[2] == 'C') and (item[0:2] + 'G' not in arriving_floor):
                is_move_valid = False
                break

        if is_move_valid:
            valid_moves.append(move)

    return valid_moves


def is_finished(state) -> bool:
    return True if (len(state[1]) + len(state[2]) + len(state[3]) == 0) else False


def gen_state(state) -> str:
    state_str = ''
    E = 'E:' + str(state[0])
    F4 = '|F4:' + str(sum([a[2] == 'C' for a in state[4]])) + 'C' + str(sum([a[2] == 'G' for a in state[4]])) + 'G'
    F3 = '|F3:' + str(sum([a[2] == 'C' for a in state[3]])) + 'C' + str(sum([a[2] == 'G' for a in state[3]])) + 'G'
    F2 = '|F2:' + str(sum([a[2] == 'C' for a in state[2]])) + 'C' + str(sum([a[2] == 'G' for a in state[2]])) + 'G'
    F1 = '|F1:' + str(sum([a[2] == 'C' for a in state[1]])) + 'C' + str(sum([a[2] == 'G' for a in state[1]])) + 'G'

    state_str = E + F4 + F3 + F2 + F1

    return state_str


def do_move(state, move):
    elevator_movement = 1 if move[1] == 'up' else -1
    for item in move[0]:
        state[state[0] + elevator_movement].append(item)
        state[state[0]].remove(item)
    state[0] += elevator_movement
    return


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    do_part_1()
    do_part_2(input_str)

    pass

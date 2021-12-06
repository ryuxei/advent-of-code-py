def make_distinct_molecules(rules: list, start: str) -> set:
    possible_new_ones = []
    for rule in rules:
        mol_from = rule.split(' => ')[0]
        mol_to = rule.split(' => ')[1]
        for i in range(0, len(start) - len(mol_from) + 1):
            if mol_from == start[i:i + len(mol_from)]:
                possible_new_ones.append(start[0:i] + mol_to + start[i + len(mol_from):len(start)])
    return set(possible_new_ones)


def reduce_to_distinct_molecules(rules: list, start: str) -> set:
    possible_new_ones = []
    for rule in rules:
        mol_from = rule.split(' => ')[0]
        mol_to = rule.split(' => ')[1]
        for i in range(0, len(start) - len(mol_to) + 1):
            if mol_to == start[i:i + len(mol_to)]:
                possible_new_ones.append(start[0:i] + mol_from + start[i + len(mol_to):len(start)])
    return set(possible_new_ones)


def transform_molecule_to_list(mol: str) -> list:
    mol_list = []
    for i in range(0, len(mol)):
        if mol[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i < len(mol) - 1 and mol[i + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                mol_list.append(mol[i][:])
            else:
                mol_list.append(mol[i:i + 2])
    mol_level = []
    curr_level = 0
    for i in range(0, len(mol_list)):
        if mol_list[i] == 'Rn':
            curr_level += 1
        mol_level.append(curr_level)
        if mol_list[i] == 'Ar':
            curr_level -= 1
    return [mol_list, mol_level]


def count_steps(mol_list: list) -> int:
    steps = 0
    return 0


if __name__ == '__main__':
    # f = open('2015day19.txt', 'r')
    # strings = f.read().splitlines()
    # f.close()

    with open('2015day19.txt', 'r') as f:
        strings = f.read().splitlines()

    rules = strings[0:43]
    # medicine = strings[44]
    medicine = 'CaSiPBCaSiThSiCaSiCaSiThCaSiCaCaSiCaPPBCaCaSiCaCaSiCaCaSiBCaCaCaCaSiThCaPBSiThPBPBCaSiSiThCaSiBCaCaSiSiThCaPBSiThCaSiPTiBCaPCaCaCaCa'

    print(len(make_distinct_molecules(rules, medicine)))

    # part 2

    mol_list = transform_molecule_to_list(medicine)

    pass

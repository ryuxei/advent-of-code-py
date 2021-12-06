def do_part_1(calls, tables, table_marks):
    for call in calls:
        for n in range(0, len(tables)):
            for i in range(0, 5):
                for j in range(0, 5):
                    if tables[n][i][j] == call:
                        table_marks[n][i][j] = '1'
                        if check_bingo(table_marks[n]):
                            print(tables[n])
                            print(cal_part_1_score(tables[n], table_marks[n], call))
                            return
    return


def do_part_2(calls, tables, table_marks):
    is_already_won = []
    for i in range(0, len(tables)):
        is_already_won.append(0)
    last_winning_table = 0
    last_winning_table_score = 0

    for call in calls:
        for n in range(0, len(tables)):
            for i in range(0, 5):
                for j in range(0, 5):
                    if tables[n][i][j] == call:
                        table_marks[n][i][j] = '1'
                        if check_bingo(table_marks[n]):
                            if is_already_won[n] != 1:
                                is_already_won[n] = 1
                                last_winning_table = n
                                last_winning_table_score = cal_part_1_score(tables[n], table_marks[n], call)
    print(tables[last_winning_table])
    print(last_winning_table_score)
    return


def parse_input(s: list) -> list:
    calls = s[0].split(',')

    tables = [[]]
    table_marks = [[]]

    for i in range(2, len(s)):
        if len(tables[-1]) == 5:
            tables.append([])
            table_marks.append([])
        if s[i] != '':
            tables[-1].append(s[i].split())
            table_marks[-1].append(['0', '0', '0', '0', '0'])

    return [calls, tables, table_marks]


def check_bingo(mark: list) -> bool:
    for i in range(0, 5):
        if mark[i] == ['1', '1', '1', '1', '1']:
            return True
        elif mark[0][i] + mark[1][i] + mark[2][i] + mark[3][i] + mark[4][i] == '11111':
            return True
    return False


def cal_part_1_score(table, mark, call) -> int:
    uncalled_sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if mark[i][j] != '1':
                uncalled_sum += int(table[i][j])

    return uncalled_sum * int(call)


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    calls, tables, table_marks = parse_input(input_str)

    do_part_1(calls, tables, table_marks)
    do_part_2(calls, tables, table_marks)

    pass

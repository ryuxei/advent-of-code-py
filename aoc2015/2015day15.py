f = open('2015day15.txt', 'r')
strings = f.read().splitlines()
f.close()

specs = [[5, -1, 0, 0, 5],
         [-1, 3, 0, 0, 1],
         [0, -1, 4, 0, 6],
         [-1, 0, 0, 2, 8]]


def get_score(comb: list, specs: list) -> int:
    cap = max(comb[0] * specs[0][0] + comb[1] * specs[1][0] + comb[2] * specs[2][0] + comb[3] * specs[3][0], 0)
    dur = max(comb[0] * specs[0][1] + comb[1] * specs[1][1] + comb[2] * specs[2][1] + comb[3] * specs[3][1], 0)
    fla = max(comb[0] * specs[0][2] + comb[1] * specs[1][2] + comb[2] * specs[2][2] + comb[3] * specs[3][2], 0)
    tex = max(comb[0] * specs[0][3] + comb[1] * specs[1][3] + comb[2] * specs[2][3] + comb[3] * specs[3][3], 0)
    cal = max(comb[0] * specs[0][4] + comb[1] * specs[1][4] + comb[2] * specs[2][4] + comb[3] * specs[3][4], 0)
    score = cap * dur * fla * tex
    return score


def get_cal(comb: list, specs: list) -> int:
    cal = max(comb[0] * specs[0][4] + comb[1] * specs[1][4] + comb[2] * specs[2][4] + comb[3] * specs[3][4], 0)
    return cal


print(get_score([4, 4, 6, 5], specs))

high_score = 0
high_score_combo = []

for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101):
            for l in range(0, 101):
                if i + j + k + l == 100:
                    print(i, j, k, l, end='\n')
                    if get_score([i, j, k, l], specs) > high_score and get_cal([i, j, k, l], specs) == 500:
                        high_score = get_score([i, j, k, l], specs)
                        high_score_combo = [i, j, k, l]

print(high_score_combo, high_score)

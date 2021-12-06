# []
def gen_perm(n):
    perm = [[0]]

    for i in range(1, n):
        new_perm = []
        for j in range(0, len(perm)):
            for k in range(i, -1, -1):
                entry = perm[j][:]
                entry.insert(k, i)
                new_perm.append(entry)
        perm = new_perm[:]

    return perm


def recursive_gen_perm(n: int) -> list:
    if n == 1:
        return [[0]]

    perm = recursive_gen_perm(n - 1)
    new_perm = []

    for j in range(0, len(perm)):
        for k in range(n - 1, -1, -1):
            entry = perm[j][:]
            entry.insert(k, n - 1)
            new_perm.append(entry)

    return new_perm


a = recursive_gen_perm(8)

pass

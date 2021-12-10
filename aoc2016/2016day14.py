import hashlib


def do_part_1(s: list):
    n = 0
    keys = []
    hash_cache = []
    while len(keys) != 64:
        curr_hash = get_hash_v2(hash_cache, n, s[0])  # get_hash() or get_hash_v2()

        triplet_letter = ''
        for i in range(0, len(curr_hash) - 2):
            if curr_hash[i] == curr_hash[i + 1] and curr_hash[i + 1] == curr_hash[i + 2]:
                triplet_letter = curr_hash[i]
                break
        if triplet_letter == '':
            n += 1
            continue

        is_valid = False
        for i in range(n + 1, n + 1001):
            h = get_hash_v2(hash_cache, i, s[0])  # get_hash() or get_hash_v2()
            for j in range(0, len(curr_hash) - 4):
                if h[j] == triplet_letter and h[j] == h[j + 1] and \
                        h[j + 1] == h[j + 2] and h[j + 2] == h[j + 3] and h[j + 3] == h[j + 4]:
                    is_valid = True
                    print('len(keys)', len(keys), 'n', n, 'curr_hash', curr_hash, 'i', i, 'i_hash', h)
                    break
            if is_valid:
                break

        if is_valid:
            keys.append(n)

        n += 1

    print(keys[-1])

    return


def do_part_2(s: list):
    return


def get_hash(hash_cache, i, salt) -> str:
    if 0 <= i < len(hash_cache):
        return hash_cache[i]
    else:
        for n in range(len(hash_cache), i + 1):
            hash_cache.append(hashlib.md5((salt + str(n)).encode()).hexdigest())
        return hash_cache[i]


def get_hash_v2(hash_cache, i, salt) -> str:
    if 0 <= i < len(hash_cache):
        return hash_cache[i]
    else:
        for n in range(len(hash_cache), i + 1):
            h = hashlib.md5((salt + str(n)).encode()).hexdigest()
            for j in range(0, 2016):
                h = hashlib.md5(h.encode()).hexdigest()
            hash_cache.append(h)
        return hash_cache[i]


if __name__ == '__main__':
    input_str = ['qzyelonm']

    do_part_1(input_str)
    do_part_2(input_str)

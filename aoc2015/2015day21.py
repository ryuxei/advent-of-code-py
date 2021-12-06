f = open('2015day21.txt', 'r')
strings = f.read().splitlines()
f.close()

boss_stats = [104, 8, 1]
player_stats = [100, 0, 0]

store = [[[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]],
         [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]],
         [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]]

shopping_cart = [0]


def is_cart_valid(curr_cart: list) -> bool:
    criteria = 0

    if len(curr_cart[0]) == 1:
        criteria += 1

    if 0 <= len(curr_cart[1]) <= 1:
        criteria += 1

    if 0 <= len(curr_cart[2]) <= 2:
        criteria += 1

    if criteria == 3:
        return True
    else:
        return False


def encode_cart(curr_cart: list) -> int:
    cart = 0
    for weapon in curr_cart[0]:
        cart += 2 ** (weapon + 11)
    for armor in curr_cart[1]:
        cart += 2 ** (armor + 6)
    for ring in curr_cart[2]:
        cart += 2 ** ring
    return cart


def decode_cart(curr_cart: int) -> list:
    cart = [[], [], []]
    for i in range(0, 5):
        if curr_cart & 2 ** (i + 11) != 0:
            cart[0].append(i)
    for i in range(0, 5):
        if curr_cart & 2 ** (i + 6) != 0:
            cart[1].append(i)
    for i in range(0, 6):
        if curr_cart & 2 ** i != 0:
            cart[2].append(i)
    return cart


def get_next_shopping_cart_combo(curr_cart: list) -> list:
    # weapon: 0,1,2,3,4
    # armor: -,0,1,2,3,4
    # rings: 000000 -> 110000
    cart = curr_cart[:]
    if cart == [0]:
        return [[0], [], []]
    if cart == [[4], [4], [4, 5]]:
        return [-1]

    cart_encoded = encode_cart(cart)
    cart_encoded += 1

    while not is_cart_valid(decode_cart(cart_encoded)):
        cart_encoded += 1

    return decode_cart(cart_encoded)


def get_price(curr_cart: list, store: list) -> int:
    total_price = 0

    for weapon in curr_cart[0]:
        total_price += store[0][weapon][0]
    for armor in curr_cart[1]:
        total_price += store[1][armor][0]
    for ring in curr_cart[2]:
        total_price += store[2][ring][0]

    return total_price


def apply_shopping_cart_to_player(player_stats: list, curr_cart: list, store: list) -> list:
    stats = player_stats[:]

    # apply weapon
    for weapon in curr_cart[0]:
        stats[1] += store[0][weapon][1]
        stats[2] += store[0][weapon][2]

    # apply armor
    for armor in curr_cart[1]:
        stats[1] += store[1][armor][1]
        stats[2] += store[1][armor][2]

    # apply rings
    for ring in curr_cart[2]:
        stats[1] += store[2][ring][1]
        stats[2] += store[2][ring][2]

    return stats


def fight(player_stats: list, boss_stats: list) -> bool:
    player_hp = player_stats[0]
    boss_hp = boss_stats[0]

    while player_hp > 0 and boss_hp > 0:
        boss_hp -= max(1, player_stats[1] - boss_stats[2])
        if boss_hp <= 0 < player_hp:
            return True
        player_hp -= max(1, boss_stats[1] - player_stats[2])
        if player_hp <= 0 < boss_hp:
            return False

    return False


lowest_cost = 0
lowest_cart = []
shopping_cart = get_next_shopping_cart_combo(shopping_cart)
while shopping_cart != [-1]:
    curr_player = apply_shopping_cart_to_player(player_stats, shopping_cart, store)
    fight_result = fight(curr_player, boss_stats)
    if not fight_result:
        cost = get_price(shopping_cart, store)
        if cost > lowest_cost:
            lowest_cost = cost
            lowest_cart = shopping_cart[:]
    shopping_cart = get_next_shopping_cart_combo(shopping_cart)

print(lowest_cost, lowest_cart)


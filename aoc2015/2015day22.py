# Magic Missile costs 53 mana. It instantly does 4 damage.
#
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
#
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
#
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active,
# it deals the boss 3 damage.
#
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active,
# it gives you 101 new mana.
#

# return:
# - 0 if turn ends
# - 1 if boss hp depleted
# - 2 if player hp depleted.
# - 3 if player mana insufficient
# - 4 if player tries to cast spell already having an effect
def do_turn(player: dict, boss: dict, whose_turn: str, action: str) -> int:
    # status overview
    # print('-- ' + whose_turn.capitalize() + ' turn --')
    # print('- Player has ' + str(player['hp']) + ' hit points, ' +
    #       str(player['armor']) + ' armor, ' + str(player['mana']) + ' mana')
    # print('- Boss has ' + str(boss['hp']) + ' hit points')

    # apply effects
    if player['shield-effect'] > 0:
        player['shield-effect'] -= 1
        # print('Shield\'s timer is now ' + str(player['shield-effect']) + '.')
        if player['shield-effect'] == 0:
            # print('Shield wears off, decreasing armor by 7.')
            player['armor'] = 0
    if boss['poison-effect'] > 0:
        boss['poison-effect'] -= 1
        # print('Poison deals 3 damage; its timer is now ' + str(boss['poison-effect']) + '.')
        boss['hp'] -= 3
        if boss['hp'] <= 0:
            # print('This kills the boss, and the player wins.')
            return 1
        if boss['poison-effect'] == 0:
            # print('Poison wears off.')
            pass
    if player['recharge-effect'] > 0:
        player['recharge-effect'] -= 1
        # print('Recharge provides 101 mana; its timer is now ' + str(player['recharge-effect']) + '.')
        player['mana'] += 101
        if player['recharge-effect'] == 0:
            # print('Recharge wears off.')
            pass

    # take actions
    if whose_turn == 'player':
        if player['total-mana-used'] > player['record-low-mana']:
            return 3
        player['hp'] -= 1
        if player['hp'] <= 0:
            return 2
        if action == 'magic-missile' or action == 'm':
            # print('Player casts Magic Missile, dealing 4 damage.')
            player['mana'] -= 53
            player['total-mana-used'] += 53
            boss['hp'] -= 4
        elif action == 'drain' or action == 'd':
            # print('Player casts Drain, dealing 2 damage and healing for 2 hit points.')
            player['mana'] -= 73
            player['total-mana-used'] += 73
            boss['hp'] -= 2
            player['hp'] += 2
        elif action == 'shield' or action == 's':
            # print('Player casts Shield, increasing armor by 7.')
            player['mana'] -= 113
            player['total-mana-used'] += 113
            player['armor'] = 7
            if player['shield-effect'] != 0:
                # print('Player casts a spell before effect ends, and is defeated.')
                return 4
            player['shield-effect'] = 6
        elif action == 'poison' or action == 'p':
            # print('Player casts Poison.')
            player['mana'] -= 173
            player['total-mana-used'] += 173
            if boss['poison-effect'] != 0:
                # print('Player casts a spell before effect ends, and is defeated.')
                return 4
            boss['poison-effect'] = 6
        elif action == 'recharge' or action == 'r':
            # print('Player casts Recharge.')
            player['mana'] -= 229
            player['total-mana-used'] += 229
            if player['recharge-effect'] != 0:
                # print('Player casts a spell before effect ends, and is defeated.')
                return 4
            player['recharge-effect'] = 5

        if player['mana'] < 0:
            # print('Player runs out of mana and is defeated.')
            return 3
    elif whose_turn == 'boss':
        if action == 'attack' or action == 'a':
            if player['armor'] == 0:
                # print('Boss attacks for ' + str(boss['damage']) + ' damage!')
                pass
            else:
                # print('Boss attacks for ' + str(boss['damage']) + ' - ' +
                #       str(player['armor']) + ' = ' + str(boss['damage'] - player['armor']) + ' damage!')
                pass
            player['hp'] -= boss['damage'] - player['armor']
        pass

    if boss['hp'] <= 0:
        # print('This kills the boss, and the player wins.')
        return 1
    elif player['hp'] <= 0:
        # print('This kills the player, and the boss wins.')
        return 2

    # print('')

    return 0


def expand_strats(curr_strat: str) -> list:
    new_strats = [curr_strat + 'm', curr_strat + 'd', curr_strat + 's', curr_strat + 'p', curr_strat + 'r']
    return new_strats


def play_game_with_strat(player: dict, boss: dict, strat: str) -> list:
    strat_outcome = [0, 0]  # final turn number, strat feasibility
    # print(strat)
    for i in range(0, len(strat)):
        # print('turn ' + str(i), end=' ')
        player_turn = do_turn(player, boss, 'player', strat[i])
        if player_turn != 0:
            strat_outcome[0] = i
            strat_outcome[1] = player_turn
            break
        boss_turn = do_turn(player, boss, 'boss', 'attack')
        if boss_turn != 0:
            strat_outcome[0] = i
            strat_outcome[1] = boss_turn
            break
        if player['total-mana-used'] > player['record-low-mana']:
            strat_outcome[1] = 3
            break
    return strat_outcome


import time

if __name__ == '__main__':
    origin_player = {'hp': 50, 'mana': 500, 'armor': 0, 'shield-effect': 0, 'recharge-effect': 0, 'total-mana-used': 0}
    origin_boss = {'hp': 55, 'damage': 8, 'poison-effect': 0}

    possible_strats = ['m', 'd', 's', 'p', 'r']

    lowest_mana_usage = 999999
    best_strat = ''

    # start_time = int(time.perf_counter())

    while len(possible_strats) > 0 and len(possible_strats[0]) < 15:
        curr_player = origin_player.copy()
        curr_player['record-low-mana'] = lowest_mana_usage
        curr_boss = origin_boss.copy()
        strat_feasibility = play_game_with_strat(curr_player, curr_boss, possible_strats[0])

        # if int(time.perf_counter()) - start_time > 1:
        #     start_time = int(time.perf_counter())
        #     print(len(possible_strats), curr_player['total-mana-used'], strat_feasibility)
        if strat_feasibility[1] == 0:
            additional_strat_branches = expand_strats(possible_strats[0])
            possible_strats += additional_strat_branches
        elif strat_feasibility[1] == 1:
            if curr_player['total-mana-used'] < lowest_mana_usage:
                lowest_mana_usage = curr_player['total-mana-used']
                best_strat = possible_strats[0]
                print(possible_strats[0], 'mana for this strat:', curr_player['total-mana-used'])
            # break
        possible_strats.pop(0)
        if len(possible_strats) > 1 and len(possible_strats[1]) > len(possible_strats[0]):
            print('current strat length:', len(possible_strats[0]), len(possible_strats))

    pass


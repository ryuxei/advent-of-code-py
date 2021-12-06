f = open('2015day24.txt', 'r')
strings = f.read().splitlines()
f.close()

packages = []
belonging_group = []
total_weight = 0

for s in strings:
    packages.append(int(s))
    total_weight += int(s)
    belonging_group.append(1)

target_group_weight = int(total_weight / 3)


def to_next_group_layout(layout: list):
    carry_one = 0
    layout[0] += 1
    for i in range(0, len(layout)):
        layout[i] += carry_one
        carry_one = 0
        if layout[i] > 3:
            layout[i] -= 3
            carry_one = 1


def count_weights(packages: list, group_layouts: list) -> list:
    weights = [0, 0, 0]
    for i in range(0, len(packages)):
        weights[group_layouts[i] - 1] += packages[27 - i]
    return weights


p = '[113, 101, 89, 83]\n[107, 103, 97, 79]\n[109, 101, 97, 79]\n[109, 103, 101, 73]\n[109, 107, 97, 73]\n[113, 103, 97, 73]\n[109, 107, 103, 67]\n[113, 109, 97, 67]\n[113, 109, 103, 61]'

p = p.splitlines()

for o in p:
    u = o[1:-1].split(', ')
    y = int(u[0]) * int(u[1]) * int(u[2]) * int(u[3])
    print(y)

import time

start_time = int(time.perf_counter())

least_group_2 = 9999
best_groups = []
two_count = 0

qwq = []

while True:
    two_count = belonging_group.count(2)
    weights = count_weights(packages, belonging_group)
    sum = 0

    nums = []
    for i in range(0, len(belonging_group)):
        if belonging_group[i] == 2:
            sum += packages[27 - i]
            nums.append(packages[27 - i])
    if sum == 387 or sum == 386:
        if nums not in qwq and len(nums) == 4:
            qwq.append(nums)
            print(belonging_group, weights, nums, sum)
    # if weights[0] == weights[1] == weights[2]:
    #     if belonging_group.count(2) < least_group_2:
    #         least_group_2 = belonging_group.count(2)
    #         best_groups = belonging_group
    #     print(two_count, belonging_group)
    # if int(time.perf_counter()) - start_time > 1:
    #     start_time = int(time.perf_counter())
    #     print(belonging_group, weights)
    to_next_group_layout(belonging_group)

pass

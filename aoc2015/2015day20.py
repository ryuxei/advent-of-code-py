inp = 34000000

import math


def get_part_1(num: int) -> int:
    house_num = 1
    while 1:
        present_num = 0
        factors = []

        for i in range(1, int(math.sqrt(house_num)) + 1):
            if house_num % i == 0:
                factors.append(i)

        remaining_factors = []
        for i in range(len(factors) - 1, -1, -1):
            if house_num != factors[i] * factors[i]:
                remaining_factors.append(int(house_num / factors[i]))

        all_non_prime_factors = factors + remaining_factors

        # for i in range(1, int(house_num / 2) + 1):
        #     if house_num % i == 0:
        #         present_num += i * 10
        # present_num += house_num * 10

        for i in range(0, len(all_non_prime_factors)):
            present_num += all_non_prime_factors[i] * 10

        if present_num >= num:
            print(house_num)
            break
        if house_num % 1000 == 0:
            print(house_num, present_num)
        house_num += 1
    return house_num


# print(get_part_1(inp))


def get_part_2(num) -> int:
    house_num = 1
    while 1:
        present_num = 0
        factors = []

        for i in range(1, int(math.sqrt(house_num)) + 1):
            if house_num % i == 0:
                factors.append(i)

        remaining_factors = []
        for i in range(len(factors) - 1, -1, -1):
            if house_num != factors[i] * factors[i]:
                remaining_factors.append(int(house_num / factors[i]))

        all_non_prime_factors = factors + remaining_factors

        for i in range(0, len(all_non_prime_factors)):
            if int(house_num / all_non_prime_factors[i]) <= 50:
                present_num += all_non_prime_factors[i] * 11

        if present_num >= num:
            print(house_num)
            break
        if house_num % 1000 == 0:
            print(house_num, present_num)
        house_num += 1
    return house_num


print(get_part_2(inp))

f = open('2021day3.txt', 'r')
strings = f.read().splitlines()
f.close()

gamma_rate = 0
epsilon_rate = 0
ones_list = []
zeros_list = []

for i in range(0, len(strings[0])):
    one_count = 0
    for j in range(0, len(strings)):
        if strings[j][i] == '1':
            one_count += 1
    one = int(one_count > int(len(strings) / 2))
    ones_list.append(str(one))
    zeros_list.append(str(1 - one))
    gamma_rate += one * (2 ** (len(strings[0]) - 1 - i))
    epsilon_rate += (1 - one) * (2 ** (len(strings[0]) - 1 - i))
    pass

print(gamma_rate * epsilon_rate)


# part 2
def do_part_2(s: list):
    oxy_gen_rating = 0
    co2_scrub_rating = 0
    list_length = len(s)
    num_length = len(s[0])

    ogen_list = s[:]
    for i in range(0, num_length):
        # get most occurring digit
        one_count = 0
        for j in range(0, len(ogen_list)):
            if ogen_list[j][i] == '1':
                one_count += 1

        most_occurring_digit = 0
        if one_count > len(ogen_list) / 2:
            most_occurring_digit = 1
        elif one_count == len(ogen_list) / 2:
            most_occurring_digit = 1
        elif one_count < len(ogen_list) / 2:
            most_occurring_digit = 0

        # pop all entry without this digit
        j = 0
        while j < len(ogen_list):
            if ogen_list[j][i] != str(most_occurring_digit):
                ogen_list.pop(j)
            else:
                j += 1

        # check if finished
        if len(ogen_list) == 1:
            oxy_gen_rating = int(ogen_list[0], 2)
            break

    co2_list = s[:]
    for i in range(0, num_length):
        # get least occurring digit
        one_count = 0
        for j in range(0, len(co2_list)):
            if co2_list[j][i] == '1':
                one_count += 1

        least_occurring_digit = 0
        if one_count > len(co2_list) / 2:
            least_occurring_digit = 0
        elif one_count == len(co2_list) / 2:
            least_occurring_digit = 0
        elif one_count < len(co2_list) / 2:
            least_occurring_digit = 1

        # pop all entry without this digit
        j = 0
        while j < len(co2_list):
            if co2_list[j][i] != str(least_occurring_digit):
                co2_list.pop(j)
            else:
                j += 1

        # check if finished
        if len(co2_list) == 1:
            co2_scrub_rating = int(co2_list[0], 2)
            break

    print('oxy_gen_rating * co2_scrub_rating: ', end='')
    print(oxy_gen_rating * co2_scrub_rating)

    return


do_part_2(strings)

pass

f = open('2015day17.txt', 'r')
strings = f.read().splitlines()
f.close()

possibilities = 0
least_nums = 21  # least num is actually 4
nums_of_least_nums = 0

for i in range(0, 2 ** 20):
    capacity = 0
    for j in range(0, len(strings)):
        if (i & 2 ** (19 - j)) != 0:
            capacity += int(strings[j])
    if capacity == 150:
        possibilities += 1
        nums_of_ones = 0
        for j in range(0, 20):
            if (i & 2 ** j) != 0:
                nums_of_ones += 1
        if nums_of_ones < least_nums:
            least_nums = nums_of_ones
        if nums_of_ones == 4:  # least num is actually 4
            nums_of_least_nums += 1

print(possibilities)
print(least_nums)
print(nums_of_least_nums)

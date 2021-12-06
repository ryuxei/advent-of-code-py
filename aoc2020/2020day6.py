f = open('2020day6.txt', 'r')
strings = f.read().split('\n\n')
f.close()

dict = 'abcdefghijklmnopqrstuvwxyz'

#  part 1
sum_of_counts = 0
for group in strings:
    count = 0
    for i in range(0, 26):
        if dict[i] in group:
            count += 1
    sum_of_counts += count

print(sum_of_counts)

#  part 2
new_sum_of_counts = 0
for group in strings:
    splitted = group.splitlines()
    no_of_people_in_group = len(splitted)
    count = 0
    for i in range(0, 26):
        if group.count(dict[i]) == no_of_people_in_group:
            count += 1
    new_sum_of_counts += count

print(new_sum_of_counts)
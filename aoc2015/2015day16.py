f = open('2015day16.txt', 'r')
strings = f.read().splitlines()
f.close()

gift_specs = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
              'trees': 3, 'cars': 2, 'perfumes': 1}

for sue in strings:
    sue_specs = sue.split(': ', maxsplit=1)[1].split(', ')
    criteria = 0
    for i in range(0, len(sue_specs)):
        obj = sue_specs[i].split(': ')[0]
        num = int(sue_specs[i].split(': ')[1])
        if obj == 'cats' or obj == 'trees':
            if num > gift_specs[obj]:
                criteria += 1
            else:
                continue
        elif obj == 'pomeranians' or obj == 'goldfish':
            if num < gift_specs[obj]:
                criteria += 1
            else:
                continue
        elif num == gift_specs[obj]:
            criteria += 1
    if criteria == len(sue_specs):
        print(sue)

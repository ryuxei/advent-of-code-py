f = open('2020day7.txt', 'r')
strings = f.read().splitlines()
f.close()


def get_bag_name(rule: str) -> str:
    for i in range(0, len(rule)):
        if rule[i:i + 3] == 'bag':
            return rule[0:i + 3]
    return ''


def is_bag_containable(rule: str, bag: str) -> bool:
    remaining_rule = ''
    for i in range(0, len(rule)):
        if rule[i:i + 4] == 'bags':
            remaining_rule = rule[i + 5:]
            break
    if bag in remaining_rule:
        return True
    else:
        return False


def add_bag_to_accepted_list(l: [], bag: str):
    for b in range(0, len(l)):
        if l[b] == bag:
            return l, 0
    l.append(bag)
    return l, 1


# part 1
new_findings = 1
accepted_bags = ['shiny gold bag']
no_of_accepted_bags = 0  # excluding the shiny gold itself

while new_findings == 1:
    new_findings = 0
    for i in range(0, len(strings)):
        for j in range(0, len(accepted_bags)):
            if is_bag_containable(strings[i], accepted_bags[j]):
                result = add_bag_to_accepted_list(accepted_bags, get_bag_name(strings[i]))
                accepted_bags = result[0]
                if new_findings == 0 and result[1] == 1:
                    new_findings = 1

print(accepted_bags)
no_of_accepted_bags = len(accepted_bags) - 1
print(no_of_accepted_bags)

# part 2
bag_num = {}  # it follows{bag_color: number_of_other_bags_required_in_it}


def sanitize_rules(rule: str):
    return rule.replace('bags', 'bag')


def get_bag_requirement(rule):
    stripped_rule = ''
    for n in range(0, len(rule)):
        if rule[n:n + 7] == 'contain':
            stripped_rule = rule[n + 8:-1]
            break
    if 'no other bag' in stripped_rule:
        return []
    else:
        rule_list = stripped_rule.split(', ')
        for n in range(0, len(rule_list)):
            rule_list[n] = rule_list[n].split(' ', maxsplit=1)
        return rule_list


def update_bag_num(rule):
    if get_bag_name(rule) in bag_num:
        return

    rules = get_bag_requirement(rule)
    curr_bag_num = 0

    for i in range(0, len(rules)):
        if rules[i][1] not in bag_num:
            return
        else:
            curr_bag_num += int(rules[i][0]) * (bag_num[rules[i][1]] + 1)

    bag_num[get_bag_name(rule)] = curr_bag_num


for i in range(0, len(strings)):
    for j in range(0, len(strings)):
        update_bag_num(sanitize_rules(strings[j]))

print(bag_num['shiny gold bag'])
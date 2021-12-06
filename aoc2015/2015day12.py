f = open('2015day12.txt', 'r')
strings = f.read().splitlines()

# part 1
import re

results = re.findall(r'-?[0-9]+', strings[0])

total = 0
for num in results:
    total += int(num)

print(total)

# part 2
import json

# store = json.loads(strings[0])
with open('2015day12.txt', 'r') as content:
    store = json.load(content)

f.close()

def count_num(obj) -> int:
    count = 0
    if isinstance(obj, list):
        for entry in obj:
            if isinstance(entry, dict) or isinstance(entry, list):
                count += count_num(entry)
            elif isinstance(entry, str):
                pass
            elif isinstance(entry, int):
                count += entry
    elif isinstance(obj, dict):
        for entry in obj:
            if isinstance(obj[entry], dict) or isinstance(obj[entry], list):
                count += count_num(obj[entry])
            elif isinstance(obj[entry], int):
                count += obj[entry]
            elif isinstance(obj[entry], str):
                if obj[entry] == 'red':
                    return 0
                pass
    return count


print(count_num(store))

pass

f = open('2020day9.txt', 'r')
strings = f.read().splitlines()
f.close()

nums = []
for string in strings:
    nums.append(int(string))

for i in range(25, len(nums)):
    pool = nums[i - 25:i]
    match = []
    for j in range(0, 24):
        if nums[i] - nums[j] in pool:
            match.append(j)
            break
    if not match:
        break

pass
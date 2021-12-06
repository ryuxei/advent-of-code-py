a = 20151125

# while 1:
#     a = (a * 252533) % 33554393

n = 0
x, y, = 0, 0
nums = []
for i in range(0, 20000):
    nums.append([])
    for j in range(0, 20000):
        nums[i].append(0)

while 1:
    if n == 15000:
        break
    if nums[2977][3082] != 0:
        print(nums[2977][3082])
    for i in range(n, -1, -1):
        nums[i][n - i] = a
        a = (a * 252533) % 33554393
    n += 1

print(nums[2977][3082])

pass

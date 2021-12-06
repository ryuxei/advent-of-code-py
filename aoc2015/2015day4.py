f = open('2015day4.txt', 'r')
strings = f.read().splitlines()
f.close()

import hashlib

md5_hash = ''

i = 1
while True:
    md5_hash = hashlib.md5((strings[0] + str(i)).encode()).hexdigest()
    if md5_hash[0:6] == '000000':
        print(i)
        break
    i += 1

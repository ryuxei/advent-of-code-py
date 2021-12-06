inp = 'reyedfim'

import hashlib

# i = 0
# while True:
#     ha = hashlib.md5((inp + str(i)).encode()).hexdigest()
#     if ha[0:5] == '00000':
#         print(ha)
#     i += 1
pas = ['', '', '', '', '', '', '', '']
i = 0
while True:
    ha = hashlib.md5((inp + str(i)).encode()).hexdigest()
    if ha[0:5] == '00000':
        if ha[5] in '01234567':
            if pas[int(ha[5])] == '':
                pas[int(ha[5])] = ha[6]
        print(ha, pas)
    i += 1

pass

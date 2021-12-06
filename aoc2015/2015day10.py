inp = '1113222113'


def look_and_say(int_as_str: str) -> str:
    new_num = ''
    count = 0
    digit = int_as_str[0]
    for i in range(0, len(int_as_str)):
        if int_as_str[i] == digit:
            count += 1
        else:
            new_num += str(count) + digit
            count = 1
            digit = int_as_str[i]
    new_num += str(count) + digit
    return new_num


for i in range(0, 50):
    inp = look_and_say(inp)

print(len(inp))
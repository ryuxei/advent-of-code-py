def day01():
    with open("./2024/day01-1.txt") as f:
        input_data = f.read().splitlines()
    s = 0
    for line in input_data:
        a, b = -1, -1
        for letter in line:
            if letter.isdigit():
                if a == -1:
                    a = int(letter)
                b = int(letter)
        c = a * 10 + b
        s += c
    print(["first answer: ", s])

    s2 = 0
    for line in input_data:
        a, b = -1, -1
        # can't use the following method because of cases
        # like 'nineight' would become 'nin8'
        # line = line.replace("one", "1")
        # line = line.replace("two", "2")
        # line = line.replace("three", "3")
        # line = line.replace("four", "4")
        # line = line.replace("five", "5")
        # line = line.replace("six", "6")
        # line = line.replace("seven", "7")
        # line = line.replace("eight", "8")
        # line = line.replace("nine", "9")
        i = 0
        while i < len(line):
            num = -1
            # check if number
            if line[i].isdigit():
                num = int(line[i])
            elif len(line) - i >= 3 and line[i : i + 3] == "one":
                num = 1
            elif len(line) - i >= 3 and line[i : i + 3] == "two":
                num = 2
            elif len(line) - i >= 5 and line[i : i + 5] == "three":
                num = 3
            elif len(line) - i >= 4 and line[i : i + 4] == "four":
                num = 4
            elif len(line) - i >= 4 and line[i : i + 4] == "five":
                num = 5
            elif len(line) - i >= 3 and line[i : i + 3] == "six":
                num = 6
            elif len(line) - i >= 5 and line[i : i + 5] == "seven":
                num = 7
            elif len(line) - i >= 5 and line[i : i + 5] == "eight":
                num = 8
            elif len(line) - i >= 4 and line[i : i + 4] == "nine":
                num = 9
            # change a and b like before
            if num != -1 and a == -1:
                a = num
            if num != -1:
                b = num
            i += 1
        c = a * 10 + b
        s2 += c
    print(["second answer: ", s2])
    return 0


if __name__ == "__main__":
    day01()
    print("hi")

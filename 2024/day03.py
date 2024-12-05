def solution():
    with open("./2024/day03.txt") as f:
        input_data = f.read().splitlines()

    s1 = 0
    for irow in range(0, len(input_data)):
        icol = 0
        while icol < len(input_data[irow]):
            if input_data[irow][icol].isdigit():
                # get right most position, j, of this number (plus one)
                j = icol + 1
                while j < len(input_data[irow]) and input_data[irow][j].isdigit():
                    j += 1
                # check all adjacent cells for symbols
                adjacent_cells_flattened = ""
                isafe, jsafe = max(0, icol - 1), min(j + 1, len(input_data[irow]))
                if irow > 0:
                    adjacent_cells_flattened += input_data[irow - 1][isafe:jsafe]
                if icol > 0:
                    adjacent_cells_flattened += input_data[irow][icol - 1]
                if j < len(input_data[irow]):
                    adjacent_cells_flattened += input_data[irow][j]
                if irow < len(input_data) - 1:
                    adjacent_cells_flattened += input_data[irow + 1][isafe:jsafe]
                if sum([int(n != '.') for n in adjacent_cells_flattened]) > 0:
                    s1 += int(input_data[irow][icol:j])
                icol = j
                continue
            icol += 1
    print(["first answer: "], s1)

    s2 = 0

    print(["second answer: "], s2)

    return 0


if __name__ == "__main__":
    solution()
    print("hi")

def solution():
    with open("./2025/day01.txt") as f:
        input_data = f.read().splitlines()

    left_list, right_list = [], []
    for line in input_data:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)
    s1 = 0
    for i in range(0, len(left_list_sorted)):
        s1 += abs(left_list_sorted[i] - right_list_sorted[i])

    print(f"first answer: {s1}")

    s2 = 0
    for i in range(0, len(left_list_sorted)):
        s2 += left_list_sorted[i] * right_list_sorted.count(left_list_sorted[i])
    
    print(f"second answer: {s2}")
    return 0


if __name__ == "__main__":
    solution()
    print("hi")

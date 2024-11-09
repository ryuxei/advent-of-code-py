def solution():
    with open("./2024/day02.txt") as f:
        input_data = f.read().splitlines()

    s1 = 0
    for game in input_data:
        game_num_rawstr, game_rounds_rawstr = game.split(": ")
        game_num = int(game_num_rawstr.split()[1])
        game_rounds = game_rounds_rawstr.split("; ")
        r_max, g_max, b_max = 0, 0, 0
        for round in game_rounds:
            cube_color_list = round.split(", ")
            for cube_color_entry in cube_color_list:
                num_of_color_str, color = cube_color_entry.split()
                if color == "red":
                    r_max = max(r_max, int(num_of_color_str))
                elif color == "green":
                    g_max = max(g_max, int(num_of_color_str))
                elif color == "blue":
                    b_max = max(b_max, int(num_of_color_str))
                else:
                    raise Exception
        if r_max <= 12 and g_max <= 13 and b_max <= 14:
            s1 += game_num
    print(["first answer: "], s1)

    s2 = 0
    for game in input_data:
        game_num_rawstr, game_rounds_rawstr = game.split(": ")
        game_num = int(game_num_rawstr.split()[1])
        game_rounds = game_rounds_rawstr.split("; ")
        r_max, g_max, b_max = 0, 0, 0
        for round in game_rounds:
            cube_color_list = round.split(", ")
            for cube_color_entry in cube_color_list:
                num_of_color_str, color = cube_color_entry.split()
                if color == "red":
                    r_max = max(r_max, int(num_of_color_str))
                elif color == "green":
                    g_max = max(g_max, int(num_of_color_str))
                elif color == "blue":
                    b_max = max(b_max, int(num_of_color_str))
                else:
                    raise Exception
        s2 += r_max * g_max * b_max
    print(["second answer: "], s2)

    return 0


if __name__ == "__main__":
    solution()
    print("hi")

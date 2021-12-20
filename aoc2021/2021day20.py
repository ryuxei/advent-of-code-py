def do_part_1(img_algo, img_grid):
    lower_bound, upper_bound = 1, 109
    for n in range(0, 2):
        new_img_grid = []
        for i in range(0, len(img_grid)):
            new_img_grid.append(img_grid[i][:])

        for i in range(lower_bound, upper_bound):
            for j in range(lower_bound, upper_bound):
                new_pixel_str = ''.join(img_grid[i - 1][j - 1:j + 2] +
                                        img_grid[i][j - 1:j + 2] +
                                        img_grid[i + 1][j - 1:j + 2])
                new_pixel_index = int(new_pixel_str.replace('.', '0').replace('#', '1'), 2)
                new_pixel = img_algo[new_pixel_index]
                new_img_grid[i][j] = new_pixel

        img_grid = new_img_grid

        lower_bound += 1
        upper_bound -= 1

    light_count = 0

    for i in range(lower_bound, upper_bound):
        for j in range(lower_bound, upper_bound):
            if img_grid[i][j] == '#':
                light_count += 1

    print(light_count)

    return


def do_part_2(img_algo, img_grid):
    lower_bound, upper_bound = 1, 301
    for n in range(0, 50):
        new_img_grid = []
        for i in range(0, len(img_grid)):
            new_img_grid.append(img_grid[i][:])

        for i in range(lower_bound, upper_bound):
            for j in range(lower_bound, upper_bound):
                new_pixel_str = ''.join(img_grid[i - 1][j - 1:j + 2] +
                                        img_grid[i][j - 1:j + 2] +
                                        img_grid[i + 1][j - 1:j + 2])
                new_pixel_index = int(new_pixel_str.replace('.', '0').replace('#', '1'), 2)
                new_pixel = img_algo[new_pixel_index]
                new_img_grid[i][j] = new_pixel

        img_grid = new_img_grid

        lower_bound += 1
        upper_bound -= 1

    light_count = 0

    for i in range(0, len(img_grid)):
        for j in range(0, len(img_grid[0])):
            print(img_grid[i][j], end='')
        print('')

    lower_bound, upper_bound = 50, 252

    for i in range(lower_bound, upper_bound):
        for j in range(lower_bound, upper_bound):
            if img_grid[i][j] == '#':
                light_count += 1

    print(light_count)

    return


def parse_input(s):
    image_enhancement_algo = s[0]

    height, width = len(s) - 2, len(s[2])
    image_grid = []

    for i in range(0, height + 10):
        image_grid.append([])
        for j in range(0, width + 10):
            if 5 <= i <= height + 4 and 5 <= j <= width + 4:
                image_grid[i].append(s[i - 3][j - 5])
            else:
                image_grid[i].append('.')

    return image_enhancement_algo, image_grid


def parse_input_v2(s):
    image_enhancement_algo = s[0]

    height, width = len(s) - 2, len(s[2])
    image_grid = []

    for i in range(0, height + 202):
        image_grid.append([])
        for j in range(0, width + 202):
            if 100 <= i <= height + 99 and 100 <= j <= width + 99:
                image_grid[i].append(s[i - 98][j - 100])
            else:
                image_grid[i].append('.')

    return image_enhancement_algo, image_grid


if __name__ == '__main__':
    with open(__file__.split('/')[-1][:-3] + '.txt') as f:
        input_str = f.read().splitlines()

    img_algo, img_grid = parse_input(input_str)
    do_part_1(img_algo, img_grid)

    img_algo_v2, img_grid_v2 = parse_input_v2(input_str)
    do_part_2(img_algo_v2, img_grid_v2)

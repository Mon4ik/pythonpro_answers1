def draw_matrix(matrix: [[int]]):
    for line in matrix:
        print(" ".join(map(str, line)))


def set_pixel(m, x, y, value):
    edited_matrix = m
    edited_matrix[y][x] = value
    return edited_matrix


def rotate_direction(direction):
    if direction[0] == 1 and direction[1] == 0:
        return [0, 1]
    if direction[0] == 0 and direction[1] == 1:
        return [-1, 0]
    if direction[0] == -1 and direction[1] == 0:
        return [0, -1]
    if direction[0] == 0 and direction[1] == -1:
        return [1, 0]


n = int(input("n: "))
m = int(input("m: "))

matrix = [[-1 for j in range(m)] for i in range(n)]
draw_matrix(matrix)

point_x, point_y = 0, 0
drew_pixels = 0
direction = [1, 0]

while drew_pixels <= n * m - 1:
    matrix = set_pixel(matrix, point_x, point_y, drew_pixels)

    future_px = point_x + direction[0]
    future_py = point_y + direction[1]

    out_of_bound = False
    in_pixel = False

    if future_px >= m or future_px < 0:
        out_of_bound = True
    elif future_py >= n or future_py < 0:
        out_of_bound = True

    if not out_of_bound:
        if matrix[future_py][future_px] != -1:
            in_pixel = True

    if out_of_bound or in_pixel:
        direction = rotate_direction(direction)

    point_x += direction[0]
    point_y += direction[1]
    drew_pixels += 1

    draw_matrix(matrix)


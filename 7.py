chessboard = [[0 for j in range(8)] for i in range(8)]

cords = input("COORD -> ").lower()
x, y = (ord(cords[0]) - 97), int(cords[1]) - 1



def set_ray(matrix, direction, sx, sy):
    m = matrix
    try:
        pos = [sx, sy]
        while True:
            pos[0] += direction[0]
            pos[1] += direction[1]

            if pos[0] > 8 or pos[0] < 0:
                break
            if pos[1] > 8 or pos[1] < 0:
                break

            m[pos[1]][pos[0]] = 2
    except:
        pass

    return m


for dirs in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
    chessboard = set_ray(chessboard, dirs, x, y)

change_to = {0: "#", 1: "Q", 2: "*"}
chessboard[y][x] = 1

for line in chessboard:
    for num in line:
        print(change_to[num], end=" ")

    print("", end="\n")
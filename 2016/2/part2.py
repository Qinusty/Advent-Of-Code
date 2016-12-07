
keys = ["  1  ",
        " 234 ",
        "56789",
        " ABC ",
        "  D  "]
xy = (0, 2)
combination = []
moves = {'L': lambda x, y: move_left(x, y),
         'R': lambda x, y: move_right(x, y),
         'U': lambda x, y: move_up(x, y),
         'D': lambda x, y: move_down(x, y)
        }


def move_left(x, y):
    if x > 0 and keys[y][x-1] != " ":
        return x-1, y
    else:
        return x, y


def move_right(x, y):
    if x < 4 and keys[y][x+1] != " ":
        return x + 1, y
    else:
        return x, y


def move_up(x, y):
    if y > 0 and keys[y-1][x] != " ":
        return x, y-1
    else:
        return x, y


def move_down(x, y):
    if y < 4 and keys[y+1][x] != " ":
        return x, y+1
    else:
        return x, y


def handle_line(line, xy):
    line = line.strip()
    for move in line:
        xy = moves[move](xy[0], xy[1])
        #print("%s : %s" % (move, keys[xy[1]][xy[0]]))
    combination.append(keys[xy[1]][xy[0]])
    return xy


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        i = 0
        for line in file:
            #print("Starting line ", i)
            i += 1
            xy = handle_line(line, xy)

    print(combination)


keys = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
xy = (1, 1)
combination = []
moves = {'L': lambda x, y: move_left(x, y),
         'R': lambda x, y: move_right(x, y),
         'U': lambda x, y: move_up(x, y),
         'D': lambda x, y: move_down(x, y)
        }


def move_left(x, y):
    if x > 0:
        return x-1, y
    else:
        return x, y


def move_right(x, y):
    if x < 2:
        return x + 1, y
    else:
        return x, y


def move_up(x, y):
    if y > 0:
        return x, y-1
    else:
        return x, y


def move_down(x, y):
    if y < 2:
        return x, y+1
    else:
        return x, y


def handle_line(line, xy):
    line = line.strip()
    for move in line:
        xy = moves[move](xy[0], xy[1])
    combination.append(keys[xy[1]][xy[0]])
    return xy


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        i = 0
        for line in file:
            i += 1
            xy = handle_line(line, xy)

    print(combination)

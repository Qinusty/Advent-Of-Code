instr = open("day1-input.txt").readlines()[0].rstrip()
##intr = "R2, R2, R2"
moves = instr.split(', ')
direction = 0

NESW = [0, 0, 0, 0]

for move in moves:
    if move[0] == 'R':
        direction += 1
        direction %= 4
    else:
        direction -= 1
        if direction < 0:
            direction = 3

    NESW[direction%4] += int(move[1:])


north = NESW[0] - NESW[2]
east = NESW[1] - NESW[3]

print(abs(north)+abs(east))


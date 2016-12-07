############################

#   This code is a mess
#   I do realise this...

######################################


instr = open("day1-input.txt").readlines()[0].rstrip()
##instr = "R8, R4, R4, R8" ### test string
moves = instr.split(', ')
direction = 0
visitted = [(0, 0), ]
x = 0
y = 0
found = None
for move in moves:
    startx, starty = x,y
    if move[0] == 'R':
        direction += 1
        direction %= 4
    else:
        direction -= 1
        if direction < 0:
            direction = 3

    if direction % 4 == 0:
        for i in range(int(move[1:])):
            y-= 1
            print(x, y)
            if (x, y) in visitted:
                print("YOU'VE ALREADY BEEN HERE")
                if found is None:
                    found = (x,y)
                break
            visitted.append((x, y))
        if found is not None: break
    elif direction % 4 == 1:
        for i in range(int(move[1:])):
            x += 1
            print(x, y)
            if (x, y) in visitted:
                print("YOU'VE ALREADY BEEN HERE")
                if found is None:
                    found = (x,y)
                break
            visitted.append((x, y))
        if found is not None: break
    elif direction % 4 == 2:
        for i in range(int(move[1:])):
            y += 1
            print(x, y)
            if (x, y) in visitted:
                print("YOU'VE ALREADY BEEN HERE")
                if found is None:
                    found = (x,y)
                break
            visitted.append((x, y))
        if found is not None: break
    else:
        for i in range(int(move[1:])):
            x -= 1
            print(x, y)
            if (x, y) in visitted:
                print("YOU'VE ALREADY BEEN HERE")
                if found is None:
                    found = (x,y)
                break
            visitted.append((x, y))
        if found is not None: break
        direction %= 4

print(abs(x)+abs(y))



def check_triangle(x,y,z):
    return x + y > z and\
        y + z > x and\
        z + x > y

if __name__ == "__main__":
    split_lines = []
    valid_triangles = []
    with open("input.txt", 'r') as file:
        for line in file:
            parts = [int(x) for x in line.strip().split()]
            split_lines.append(parts)

    for i in range(3):
        for j in range(int(len(split_lines)/3)):
            x,y,z = split_lines[j*3][i], split_lines[j*3+1][i], split_lines[j*3+2][i]
            if check_triangle(x,y,z):
                valid_triangles.append(tuple(parts))
    print(len(valid_triangles))
    print(valid_triangles)
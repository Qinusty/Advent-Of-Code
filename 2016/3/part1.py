
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
            if check_triangle(parts[0], parts[1], parts[2]):
                valid_triangles.append(tuple(parts))
    print(len(valid_triangles))
    print(valid_triangles)
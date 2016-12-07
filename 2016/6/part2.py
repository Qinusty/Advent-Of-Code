
def most_frequent_in_col(lines, col):
    freq_map = {}
    for line in lines:
        line = line.strip()
        char = line[col]
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    most_frequent = sorted(freq_map.items(), key=lambda i: i[1], reverse=False)[0]
    return most_frequent[0]



if __name__ == '__main__':
    lines = []
    output = []
    with open('input.txt') as file:
        lines = file.readlines()
    for col in range(len(lines[0])-1):
        output.append(most_frequent_in_col(lines, col))
    output = ''.join(output)
    print(output)

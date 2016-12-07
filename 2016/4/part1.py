def split_room_data(room):
    room = room.strip()
    checksum = ""
    cipher_text = ""
    sector_id = 0
    parts = room.split('[')
    checksum = parts[1].strip(']')
    parts = parts[0]
    parts = ''.join(parts).split('-')
    sector_id = int(parts[-1:][0])
    cipher_text = ''.join(parts[:-1])
    return sector_id, cipher_text, checksum


def valid_room(cipher_text, checksum):
    freq_map = make_frequency_map(cipher_text)
    sorted_list = sorted(freq_map, key=lambda pair: (-pair[1], pair[0]), reverse=False)
    for i in range(len(checksum)):
        if not sorted_list[i][0] == checksum[i]:
            return False
    return True


def make_frequency_map(cipher_text):
    chars = []
    freqs = []
    for char in cipher_text:
        if char in chars:
            freqs[chars.index(char)] += 1
        else:
            freqs.append(1)
            chars.append(char)
    return zip(chars, freqs)

if __name__ == "__main__":
    total = 0
    with open('input.txt') as file:
        for room in file:
            sec_id, cipher_text, checksum = split_room_data(room)
            if valid_room(cipher_text, checksum):
                total += sec_id
    print(total)

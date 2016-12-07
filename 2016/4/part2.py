alphabet = "abcdefghijklmnopqrstuvwxyz"

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

def get_real_data(file):
    valid_rooms = []
    for room in file:
        sec_id, cipher_text, checksum = split_room_data(room)
        if valid_room(cipher_text, checksum):
            valid_rooms.append((sec_id, cipher_text, checksum))
    return valid_rooms

def decypher_text(cipher_text, n):
    output = ""
    for char in cipher_text:
        new_index = (alphabet.index(char)+n) % 26
        output += alphabet[new_index]
    return output

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    with open('input.txt') as file:
        rooms = get_real_data(file)
        for room in rooms:
            dec_room = decypher_text(room[1], room[0])
            if 'north' in dec_room or 'pole' in dec_room:
                print("%d -> %s" % (room[0], dec_room))


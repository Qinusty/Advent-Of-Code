import hashlib



def create_password(door_id):
    passwd = [' ' for _ in range(8)]
    n = 0
    set_values = set()
    while len(set_values) < 8:
        hex = ""
        while not hex.startswith('00000'):
            m = hashlib.md5()
            m.update((door_id + str(n)).encode())
            hex = m.hexdigest()
            n += 1

        index = int(hex[5], 16)
        if index < 8 and index not in set_values:
            passwd[index] = hex[6]
            set_values.add(index)
            print(door_id, n-1, " -> %s" % hex, sep='')
    return ''.join(passwd)

if __name__ == '__main__':
    INPUT = 'abbhdwsy'
    print(create_password(INPUT))

#05ace86b
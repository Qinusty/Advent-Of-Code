import hashlib



def create_password(door_id):
    passwd = ""
    n = 0
    for i in range(8):
        hex = ""
        while not hex.startswith('00000'):
            m = hashlib.md5()
            m.update((door_id + str(n)).encode())
            hex = m.hexdigest()
            n += 1
        passwd += hex[5]
    return passwd

if __name__ == '__main__':
    INPUT = 'abbhdwsy'
    print(create_password(INPUT))


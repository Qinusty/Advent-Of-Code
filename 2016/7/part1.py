

def supports_tls(ip):
    ip = ip.strip()
    hypernet = False
    got_abba = False
    for i in range(len(ip)):
        if ip[i] == '[':
            hypernet = True
        elif ip[i] == ']':
            hypernet = False
        this2 = ip[i:i+2]
        next2 = ip[i+2:i+4][::-1]

        if this2 == next2 and this2[0] != this2[1]:
            if hypernet:
                return False
            else:
                got_abba = True
    return got_abba

if __name__ == '__main__':
    num_support_tls = 0
    with open('input.txt') as file:
        for line in file:
            if supports_tls(line):
                num_support_tls += 1
    print(num_support_tls)

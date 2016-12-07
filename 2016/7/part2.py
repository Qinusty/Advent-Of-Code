

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

def supports_ssl(super_seqs, hyper_seqs):
    babs = []
    for seq in super_seqs:
        for i in range(len(seq)):
            chunk = seq[i:i+3]
            if len(chunk) > 2:
                if chunk[0] == chunk[2] and chunk[0] != chunk[1]:
                    babs.append(''.join([chunk[1], chunk[0], chunk[1]]))
    if len(babs) > 0:
        for seq in hyper_seqs:
            for bab in babs:
                if bab in seq:
                    return True
    return False

def split_ip(ip):
    supernet_seqs = []
    hypernet_seqs = []
    cur_supernet = []
    cur_hypernet = []
    in_hypernet = False
    for char in ip:
        if char == '[':
            supernet_seqs.append(''.join(cur_supernet))
            cur_supernet = []
            in_hypernet = True
            continue
        elif char == ']':
            hypernet_seqs.append(''.join(cur_hypernet))
            cur_hypernet = []
            in_hypernet = False
            continue
        else:
            if in_hypernet:
                cur_hypernet.append(char)
            else:
                cur_supernet.append(char)
    if len(cur_supernet) > 0:
        supernet_seqs.append(''.join(cur_supernet))
    if len(cur_hypernet) > 0:
        hypernet_seqs.append(''.join(cur_hypernet))
    return supernet_seqs, hypernet_seqs


if __name__ == '__main__':
    num_support_ssl= 0
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            s_seqs, h_seqs = split_ip(line)
            if supports_ssl(s_seqs, h_seqs):
                num_support_ssl += 1
    print(num_support_ssl)

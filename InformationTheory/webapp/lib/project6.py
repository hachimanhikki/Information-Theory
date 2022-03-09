


def find_error(seq):
    m = 4
    s = 7
    final_seq = ''
    index = {
        '001': 6,
        '010': 5,
        '011': 3,
        '100': 4,
        '101': 0,
        '110': 2,
        '111': 1
    }
    while len(seq) >= s:
        temp = list(seq[:s])
        seq = seq[s:]
        e1 = int(temp[4]) ^ int(temp[0]) ^ int(temp[1]) ^ int(temp[2])
        e2 = int(temp[5]) ^ int(temp[1]) ^ int(temp[2]) ^ int(temp[3])
        e3 = int(temp[6]) ^ int(temp[0]) ^ int(temp[1]) ^ int(temp[3])
        e = f"{e1}{e2}{e3}"
        if e != '000':
            temp[index[e]] = f"{1 - int(temp[index[e]])}"
        final_seq += ''.join(temp[:m])
    return final_seq


def get_result(seq):
    final_seq = find_error(seq)
    return final_seq


# def main():
#     final_seq = get_result()
#     decoded = project3.get_result(final_seq)
#     print(final_seq)
#     print()
#     print(decoded)


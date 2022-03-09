

def hamming_encode(seq):
    # hamming (7, 4)
    m = 4
    final_seq = ''
    while 0 < len(seq) < m:
        seq += '0'
    while len(seq) >= m:
        temp = seq[:m]
        seq = seq[m:]
        r1 = int(temp[0]) ^ int(temp[1]) ^ int(temp[2])
        r2 = int(temp[1]) ^ int(temp[2]) ^ int(temp[3])
        r3 = int(temp[0]) ^ int(temp[1]) ^ int(temp[3])
        final_seq += f"{temp}{r1}{r2}{r3}"
        while 0 < len(seq) < m:
            seq += '0'
    return final_seq


def get_result(seq):
    final_seq = hamming_encode(seq)
    return final_seq


def main():
    print(get_result())

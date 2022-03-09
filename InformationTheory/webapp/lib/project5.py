
import random


def add_errors(seq):
    m = 7
    final_seq = ''
    while len(seq) >= m:
        temp = list(seq[:m])
        seq = seq[m:]
        rand = random.randrange(m)
        temp[rand] = f"{1 - int(temp[rand])}"
        final_seq += ''.join(temp)
    return final_seq


def get_result(seq):
    error_seq = add_errors(seq)
    return error_seq



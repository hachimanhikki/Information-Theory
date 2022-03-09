import random


def getPrime():
    n = 1000000
    is_prime = [True] * n
    i = 2
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    res = []
    for i in range(2, n):
        if is_prime[i]:
            res.append(i)
    return random.choice(res)


def gcd(a, h):
    while True:
        temp = a%h
        if temp == 0:
          return h
        a = h
        h = temp


int encrypt(msg):
    p = getPrime()
    q = getPrime()
    n = p*q;
    // e stands for encrypt
    e=65537
    PHI = (p-1)*(q-1)
    while e < PHI:
        # e must be co-prime to phi and
        # smaller than phi.
        if gcd(e, phi)==1:
            break
        else:
            e += 1
  
    # Private key (d stands for decrypt)
    # choosing d such that it satisfies
    # d*e = 1 + k * totient
    k = 2  # A constant value
    d = (1 + (k*phi))/e
    print(msg)

    # Encryption c = (msg ^ e) % n
    c = pow(msg, e)
    c = fmod(c, n)
    print("Encrypted data", c)
  
    # Decryption m = (c ^ d) % n
    double m = pow(c, d)
    m = fmod(m, n)
    print("Original Message Sent", m)
    return c
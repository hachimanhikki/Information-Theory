from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 
import Crypto
import libnum


def encrypted_text(msg):
	bits=128
	p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
	q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
	n = p*q
	PHI=(p-1)*(q-1)
	e=65537
	d=libnum.invmod(e,PHI)
	m=bytes_to_long(msg.encode('utf-8'))
	# Encryption c = (msg ^ e) % n
	c=pow(m, e, n)
	# Decryption res = (c ^ d) % n
	res=pow(c, d ,n)
	return str(res)



def encrypt(msg):
	bits=128
	p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
	q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
	n = p*q
	PHI=(p-1)*(q-1)
	e=65537
	d=libnum.invmod(e,PHI)
	m=bytes_to_long(msg.encode('utf-8'))
	# Encryption c = (msg ^ e) % n
	c=pow(m, e, n)
	return str(c), d, e, n, PHI

def decrypt(c, d, n):
	res=pow(c, d ,n)
	res = int(res)
	return long_to_bytes(res)
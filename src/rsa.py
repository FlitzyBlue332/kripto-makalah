import random
from math import gcd
from Crypto.Util.number import isPrime, inverse

# program ini hanya menerima dan mengeluarkan bilangan bulat
def totient(p, q):
    return (p-1)*(q-1)

def generate_prime_number():
    while True:
        p = random.randint(10**50, 10**100)
        if isPrime(p):
            return p
        
def generate_key_pair(p, q):
    '''
    menghasilkan public key, private key
    '''
    n = p * q
    m = totient(p, q)

    while True:
        e = random.randint(1, m-1)
        if gcd(e, m) == 1:
            break
    d = inverse(e, m)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = pow(plaintext, key, n)
    return cipher

def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = pow(ciphertext, key, n)
    return plain

def encypttext(public_key, plaintext):
    key, n = public_key
    cipher = pow(plaintext, key, n)
    return cipher
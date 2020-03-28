"""
This is Simple ElGamal encoding.
ElGamal's algorithm is based on the difficulties of computing the discrete logarithm.
Public key - (a,p,y)
Private key - (x)

Encoding procedure:
    Y = a ^ k mod p
    G = M * y^k (mod p)
    CipherText = (Y,G)

Decoding procedure:
    M = Y ^ (-x) * G (mod p)

Where:
    p: Prime number
    a: Primitive root modulo p
    x: The number a in the interval (1, p) is coprime to p-1
    y: a^x mod p

"""


def get_prime_number():
    pass


def generate_key():
    pass


def get_primitive_root(p):
    pass


def get_coprime_number(p):
    pass


def encode(message, a, p, y):
    pass


def decode(Y, G, x, p):
    pass

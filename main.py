"""
This is Simple ElGamal encoding.
ElGamal's algorithm is based on the difficulties of computing the discrete logarithm.
Public key - (y)
Private key - (x)

Encoding procedure:
    a = g ^ k mod p
    b = M * y^k (mod p)
    CipherText = (a,b)

Decoding procedure:
    M = b * a^(p-1-x) (mod p)

Where:
    p: Prime number
    g: Primitive root modulo p
    x: The number a in the interval (1, p) is coprime to p-1
    y: g^x mod p
    k: session key
    M: message

!! Important note: p should be greater that M

"""
import random
import os, sys
from datetime import datetime
from base64 import b64decode, b64encode
from Operations import fast_pow, is_coprime, is_prime

minimal_p = 2 ** 8
maximum_p = 2 ** 9


class SafeDict(dict):
    def __missing__(self, key):
        return []


class ElGamal:
    def __init__(self):
        self.primes = []
        self.roots = SafeDict()
        self.coprimes = SafeDict()

    def generate_keys(self):
        print("Generates keys")
        p = self.get_prime_number()
        g = self.get_primitive_root(p)
        x = self.get_coprime_number(p - 1)
        y = fast_pow(g, x) % p
        return p, g, y, x

    def get_prime_number(self):
        print("Calculates prime")
        if not self.primes:
            self.primes = [i for i in range(minimal_p, maximum_p, 1) if is_prime(i)]
        return random.choice(self.primes)

    def get_primitive_root(self, p):
        print("Calculates primitive roots")
        if not self.roots[p]:
            required_set = {num for num in range(1, p) if is_coprime(num, p)}
            self.roots[p] = [g for g in range(1, p) if required_set == {pow(g, powers, p)
                                                                        for powers in range(1, p)}]
        return random.choice(self.roots)

    def get_coprime_number(self, p):
        print("Calculates coprime")
        if not self.coprimes[p]:
            for num in [i for i in range(1, p)]:
                if is_coprime(num, p):
                    self.coprimes[p].append(num)
        return random.choice(self.coprimes[p])

    def encode(self, message, public_key=None):
        if not public_key:
            self.generate_keys()
        k = self.get_coprime_number(p - 1)
        a = fast_pow(g, k) % p
        b = message * fast_pow(y, k) % p
        return (a, b)

    def decode(self, Y, G, x, p):
        message = (fast_pow(Y, -x) * G) % p
        return message


class CipherText:
    def __init__(self):
        pass


class PublicKey:
    def __init__(self, p, g, y):
        self.p = p
        self.g = g
        self.y = y
        self.public_key = None

    def save_public_key(self):
        os.system('')

    def _to_string(self):
        string = f'{self.p}, {self.g}, {self.y}'
        self.public_key = b64encode(string.encode('utf-8'))

    def _from_string(self):
        string = b64decode(self.public_key)
        self.p, self.g, self.y = string.split(',')


class PrivateKey:
    def __init__(self, p=None, x=None):
        self.p = p
        self.x = x


elgamal = ElGamal()

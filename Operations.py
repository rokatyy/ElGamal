from math import gcd


def is_prime(num):
    for i in range(2, int(num ** 1/2)):
        if (num % i) == 0:
            return False
    return True


def is_coprime(x, y):
    if gcd(x, y) == 1:
        return True
    else:
        return False


def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p

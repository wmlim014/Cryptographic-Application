""" 
    This file is to make sure the `publickey.txt` and private key provided as valid
    RSA Algorithm in Cryptography: https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
"""
import sympy

min, max = 0, 200
publickey_path = "Task5/publickey.txt"

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys():
    """ Public Key = (e, pq)
        e is relatively to (p-1)(q-1), where
        gcd((p-1)(q-1), e)
    """
    # Generate p and q randomly
    p = sympy.randprime(min, max)
    q = sympy.randprime(min, max)

    pq = p * q
    phi = (p - 1) * (q - 1)
    print(f"p = {p}, q = {q}, phi = {phi}")

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    """ Private Key = (d, pq)
        ed = 1 mod ((p-1)(q-1))
        d = e^(-1) mod ((p-1)(q-1))
    """
    d = modInverse(e, phi)

    return e, d, pq

def writeFile():
    e1, d1, pq1 = generateKeys()
    e2, d2, pq2 = generateKeys()

    f = open(publickey_path, "w") # Open file and overwrite
    f.write(f"{e1}\n{pq1}\n{e2}\n{pq2}")
    f.close()

    # open and read the file after the overwriting:
    f = open(publickey_path, "r")
    print(f"\nPublic key: e1, n1, e2, n2")
    print(f.read())

    print(f"\nPrivate key: ({d1}, {pq1}); ({d2}, {pq2})")
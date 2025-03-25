
import hashlib
import random
import json
import os
from Task5.publickeyGen import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

msg_path = "Task5/message.txt"
publickey_path = "Task5/publickey.txt"
signature_path = "Task5/signature.txt"

def readKeys():
    """ Read In Public Key"""
    with open(publickey_path, "r") as f:
        e1 = int(f.readline().strip())
        n1 = int(f.readline().strip())
        e2 = int(f.readline().strip())
        n2 = int(f.readline().strip())
    return (e1, n1), (e2, n2)

def readMessage():
    with open(msg_path, "r") as f:
        return f.read().strip()

def aesEncryptBytes(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data, AES.block_size))

def aesDecryptBytes(encrypted_data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(encrypted_data), AES.block_size)

def generateV(key):
    v = os.urandom(16)  # Generate random v (16 bytes)
    v = aesEncryptBytes(v, key) # Encrypt v
    return v

def computeY(k: bytes, v_bytes: int, yx: int, n: int) -> int:
    # Convert yx and v to 16-byte blocks
    yx_bytes = yx.to_bytes(16, 'big')
    
    # Compute XOR(yx, v)
    xor_yx_v = bytes([a ^ b for a, b in zip(yx_bytes, v_bytes)])
    
    # Encrypt to get C = E_k(XOR(yx, v))
    C = aesEncryptBytes(xor_yx_v, k)
    
    # Compute y2 = XOR(s, C), where s = D_k(v)
    s = aesDecryptBytes(v_bytes, k)
    y2_bytes = bytes([a ^ b for a, b in zip(s, C)])
    y2 = int.from_bytes(y2_bytes, 'big') % n  # Ensure y2 < n
    
    print(f"yx_bytes: {yx_bytes}")
    print(f"xor_yx_v: {xor_yx_v}")
    print(f"C: {C}")
    print(f"s: {s}")
    print(f"y2_bytes: {y2_bytes}")
    print(f"y2: {y2}")

    return y2

def computeYx(e, n):
    ''' Calculate Yx = (Xx)^Ex mod Nx'''
    # Pick random x1 for User-1 that are smaller than n1
    x = random.randint(1, n)
    # Fast method to compute (a ^ b) mod p
    y = pow(x, e, n)
    return x, y

def sign(user, private_key):
    (e1, n1), (e2, n2) = readKeys()
    P1 = (e1, n1)
    P2 = (e2, n2)
    message = readMessage()
    
    # Compute key k = H(m)
    key = hashlib.sha256(message.encode()).digest()[:16]

    if user == 2: # User-2 is the signer
        # Pick a random glue value v that are smaller than n2
        v = generateV(key)
        x1, y1 = computeYx(e1, n1)
        y2 = computeY(key, v, y1, n2)
        # Fast method to compute (a ^ b) mod p
        x2 = pow(y2, private_key, n2)
        print(f"y1 = {y1}, y2 = {y2}, x1 = {x1}, x2 = {x2}") # Debbug line
    
    else: # User-1 is the signer
        v = generateV(key)
        x2, y2 = computeYx(e2, n2)
        y1 = computeY(key, v, y2, n1)
        # Fast method to compute (a ^ b) mod p
        x1 = pow(y1, private_key, n1)
        print(f"y1 = {y1}, y2 = {y2}, x1 = {x1}, x2 = {x2}") # Debbug line
    
    outputSignature(P1, P2, v, x1, x2)

def outputSignature(P1, P2, v, x1, x2):
    signature = {
        "P1": P1, 
        "P2": P2, 
        "v": int.from_bytes(v, 'big') % (1 << 128), # Ensure v is 128 bits (16 bytes)
        "x1": x1,
        "x2": x2
    }

    with open(signature_path, "w") as f:
        json.dump(signature, f)
    print("Signature generated and saved in folder name: Task5")

def requestPrivateKey():
    user = int(input("Enter Signer (1 or 2): "))
    private_key = int(input("Enter your private key: "))
    return user, private_key
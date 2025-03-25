from Task5.sign import *

def readFiles():
    (e1, n1), (e2, n2) = readKeys()
    message = readMessage()

    with open(signature_path, "r") as f:
        signature = json.load(f)

    P1 = signature["P1"]
    P2 = signature["P2"]
    v = signature["v"]
    x1 = signature["x1"]
    x2 = signature["x2"]

    return P1, P2, v, x1, x2, message

def verify():

    P1, P2, v, x1, x2, message = readFiles()
    # Fast method to compute (a ^ b) mod p
    y1 = pow(x1, P1[0], P1[1])
    y2 = pow(x2, P2[0], P2[1])
    # y1 = x1 % P1[1]
    # y2 = x2 % P2[1]


    # Compute Key, k = H(m)
    # AES Key Size = 128 (for 10 Rounds)
    key = hashlib.sha256(message.encode()).digest()[:16]
    
    # Convert y1 and v to bytes
    y1_bytes = y1.to_bytes(16, 'big')
    v_bytes = v.to_bytes(16, 'big')

    # Compute XOR(y1, v) and encrypt to get C
    xor_y1_v = bytes([a ^ b for a, b in zip(y1_bytes, v_bytes)])
    C = aesEncryptBytes(xor_y1_v, key)

    # Compute XOR(y2, C) and encrypt to check against v
    y2_bytes = y2.to_bytes(16, 'big')
    xor_y2_C = bytes([a ^ b for a, b in zip(y2_bytes, C)])
    computed_v_bytes = aesEncryptBytes(xor_y2_C, key)
    computed_v = int.from_bytes(computed_v_bytes, 'big') % (1 << 128)

    print(f"V: {v}\nComputed V: {computed_v}") # Debug Line

    return computed_v == v

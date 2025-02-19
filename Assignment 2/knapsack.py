from myInfo import *
from Task3.task3ValidateFuncs import *

def privateKey(n):
    '''2. Asks user to enter the value for n(i) as private key'''
    private_keys = []

    for i in range(1, n + 1):
        increaseKnapsack = int(input(f"Enter value {i} for private key: "))
        private_keys.append(increaseKnapsack)

    isSuperIncreasing(private_keys)
    print()
    return private_keys

def generatePublicKey(private_keys, m, mod): 
    ''' 
        Calculate the valus of the public key using:
        - valided private key
        - satisfied multipier
        - modulus
        (private_key * satisfied_multipier) modular mod
    '''
    public_keys = []
    for curr_pk in private_keys:
        public_key = (curr_pk * m) % mod
        public_keys.append(public_key)
    return public_keys

def encrypt(input_binary, public_keys):
    ''' Multiply each value of the public key with the corresponding 
        values of each group and take their sum 
    '''
    encrypted_total = 0
    for i in range(0, len(input_binary) - 1):
        curr = input_binary[i] * public_keys[i]
        encrypted_total = encrypted_total + curr
    
    return encrypted_total

def decrypt(ciphertext, private_keys, m, mod):
    ''' Decryption process:
        1. Find multiplicative inverse of m modulo mod (n-1)
            x = ciphertext * (n-1) modulo mod
        2. Make the sum of x from the values of private key
            e.g. 1 + 10 = 11, 
                 make the corresponding bits 1 and others 0
    '''
    # Multiplicative inverse of m modulo mod (n-1)
    m_inverse = pow(m, -1, mod)
    decrypted_msg = ''
    x = (ciphertext * m_inverse) % mod
    # print(m_inverse, x) # Debbug line 

    for pk in reversed(private_keys):
        if x >= pk:
            decrypted_msg = '1' + decrypted_msg
            x -= pk # Update new x

        else:
            decrypted_msg = '0' + decrypted_msg

        # print(f"Current private key: {pk}; Current decrypted msg: {decrypted_msg}") # Debbug line

    return decrypted_msg

def knapsackSetup():
    # 1. Asks for the number of size for the super-increasing knapsack
    n = int(input("Enter the size of super-increasing knapsack: "))
    private_keys = privateKey(n) # 2. Request private key from user

    # 3. Get modulus and multiplier from user
    mod = int(input("Enter a modulus value: "))
    multiplier = int(input("Enter a multiplier value: "))
    # Check if the multiplier satisfied
    validateModular(multiplier, mod, private_keys) 

    # 4. Generate the public keys
    public_keys = generatePublicKey(private_keys, multiplier, mod)
    print(f"Public key generated: {public_keys}\n")

    return n, private_keys, multiplier, mod, public_keys

def requestEncryptMessage(size, public_keys):
    plaintext = input(f"Enter a binary message of length {size}: ")
    # Split user input into digits with map()
    plaintexts = list(map(int, plaintext.strip())) 
    # print (len(plaintexts)) # Debbug line
    validatePlainText(size, plaintexts) # Check validation for the plaintext
    encrypted_msg = encrypt(plaintexts, public_keys)

    return encrypted_msg
    
def requestDecryptMessage(private_keys, m, mod):
    ciphertext = int(input("Enter a ciphertext to decrypt: "))
    decrypted_msg = decrypt(ciphertext, private_keys, m, mod)

    return decrypted_msg

if __name__ == "__main__":
    myInfo("Task 3", [
            "1. Knapsack Algorithm in Cryptography: https://www.geeksforgeeks.org/knapsack-encryption-algorithm-in-cryptography/", 
            "2. Split a digits into list: https://www.geeksforgeeks.org/python-split-a-list-having-single-integer/"])
    
    ''' Tested with the following:
            private key = {1, 2, 4, 10, 20, 40}
            mod = 110, multiplier = 31
            public key = {31, 62, 14, 90, 70, 30} 
            encryption message: (result - 121 197 205)
            100100  <--> 121
            111100  <--> 197
            101110  <--> 205
    '''
    size, private_keys, multiplier, mod, public_keys = knapsackSetup()
    
    # Encryption process
    ciphertext = requestEncryptMessage(size, public_keys)
    print(f"Ciphertext: {ciphertext}\n")

    # Decryption process
    decrypted_msg = requestDecryptMessage(private_keys, multiplier, mod)
    print(f"Decrypted Message: {decrypted_msg}\n")

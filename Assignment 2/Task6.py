from myInfo import *
import random

def isPrime(x):
    # Negative numbers, 0 and 1 are not primes
    if x > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (x // 2) + 1):
        
            # If x is divisible by any number between
            # 2 and x / 2, it is not prime
            if (x % i) == 0:
                print("Invalid Key. Prime number is required for security in the Diffie-Hellman key exchange.")
                print("Existing...")
                exit()

def keyGenerator(K1, x, K2):
    """ Return value of K1^x mod K2 """
    if x == 1:
        return K1
    else:
        return pow(K1, x) % K2

def requestPublicPara():
    """ A = prime number, B = primitive root of A"""
    A = int(input("Enter a prime integer: "))
    isPrime(A)  # Check if A is prime
    private_keyA = random.randint(2, A - 2) # Random generate a prime number
    # private_keyA = 65 # Debbug line

    B = int(input("Enter a integer: "))
    # isPrime(B)  # Check if B is prime
    private_keyB = random.randint(2, B - 2) # Random generate a prime number
    # private_keyB = 175 # Debbug line

    return A, B, private_keyA, private_keyB

def keyExchangeProcessing(A, B, private_keyA, private_keyB):
    # Generating key for exchange 
    generated_KeyA = keyGenerator(B, private_keyA, A)
    generated_KeyB = keyGenerator(B, private_keyB, A)

    # After keys exchanged, generating secret key
    # Secret key for A with exchanged key from B, private key generated for A and Public number A
    secretA = keyGenerator(generated_KeyB, private_keyA, A)
    # Secret key for B with exchanged key from A, private key generated for B and Public number A
    secretB = keyGenerator(generated_KeyA, private_keyB, A)

    return generated_KeyA, generated_KeyB, secretA, secretB

def manInMiddle(A, B, i):
    # Generating random private number selected for Person 1
    private_keyA = random.randint(2, A - 2) # Random generate a prime number
    private_keyB = random.randint(2, A - 2) # Random generate a prime number
    private_keys = [private_keyA, private_keyB] # Store generated keys

    # Computing public values -> Exchanged key
    public = keyGenerator(B, private_keys[i], A)

    return private_keys[i], public
            
if __name__ == '__main__':
    myInfo("Task 4", [
            "1. Implementation of Diffie-Hellman Algorithm: https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/", 
            "2. Check Prime Number: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/", 
            "3. Man in the Middle attack: https://www.geeksforgeeks.org/man-in-the-middle-attack-in-diffie-hellman-key-exchange/"])
    
    A, B, private_keyA, private_keyB = requestPublicPara()
    public_keyA, public_keyB, secretA, secretB = keyExchangeProcessing(A, B, private_keyA, private_keyB)
    
    print("Secret key for Person 1 is: ", secretA)
    print("Secret key for Person 2 is: ", secretB)


    # Start man-in-the-middle-attack
    print("\nSteps for man-in-the-middle-attack: ")
    print("----------------------------------------------------\n")
    print(f"2 prime public integers selected from both person are {A}, {B}\n")

    print("Private key generated for Person 1: ", private_keyA)
    print("Private key generated for Person 2: ", private_keyB)

    keyA, publicA = manInMiddle(A, B, 0)
    print("ManInMiddle selected private for Person 1: ", keyA)
    keyB, publicB = manInMiddle(A, B, 1)
    print("ManInMiddle selected private for Person 2: ", keyB)

    print("\nPublic key generated for Person 1: ", public_keyA)
    print("Public key generated for Person 2: ", public_keyB)

    print("ManInMiddle selected Public for Person 1: ", publicA)
    print("ManInMiddle selected Public for Person 2: ", publicB)

    secretA = keyGenerator(publicA, private_keyA, A)
    secretMA = keyGenerator(public_keyA, keyA, A)
    print("\nPerson 1 secret: ", secretA)
    print("ManInMiddle computed secret for Person 1: ", secretMA)

    secretB = keyGenerator(publicB, private_keyB, A)
    secretMB = keyGenerator(public_keyB, keyB, A)
    print("\nPerson 2 secret: ", secretB)
    print("ManInMiddle computed secret for Person 2: ", secretMB)

from myInfo import *
# from Task6.preventMitM import *
import random
import secrets
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

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

def generateRSAKeypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def signMessage(private_key, message):
    rsa_key = RSA.import_key(private_key)
    message = str(message).encode()
    h = SHA256.new(message)
    signature = pkcs1_15.new(rsa_key).sign(h)
    return base64.b64encode(signature)

def verifySignature(public_key, message, signature):
    rsa_key = RSA.import_key(public_key)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(rsa_key).verify(h, base64.b64decode(signature))
        return True
    except (ValueError, TypeError):
        return False

def keyGenerator(K1, x, K2):
    """ Return value of K1^x mod K2 """
    if x == 1:
        return K1
    else:
        return pow(K1, x, K2)

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

def manInMidWSign(public_keyA, public_keyB):
    # Eva use system auto generate the private and public key with RSA algorithm for both user
    eva_private1, eva_public1 = generateRSAKeypair()
    eva_private2, eva_public2 = generateRSAKeypair()
    print("""Eva generated new RSA key pair for Person 1 and 2
    because he not manage to return RSA private key from their RSA public key""")
    # Eva add signature with private keys generated from RSA key pair 
    # and public key input from user
    signed_pubkey1 = signMessage(eva_private1, public_keyA)
    signed_pubkey2 = signMessage(eva_private2, public_keyB)
    print("""Eva add signature process for Person 1 and 2 completed 
    with private key generated from combination of RSA key pair and theirs own public key\n""")
    
    # print("\neva signed message for P1: ", signed_pubkey1) # Debbug line
    # print("\neva signed message for P2: ", signed_pubkey2) # Debbug line

    return signed_pubkey1, signed_pubkey2

def mainWithMitM(private_keyA, private_keyB, public_keyA, public_keyB, A, B):
    
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


def withPreventionProcess(private_keyA, private_keyB, public_keyA, public_keyB, A, B):
   
    # System auto generate the private and public key with RSA algorithm
    private1, public1 = generateRSAKeypair()
    private2, public2 = generateRSAKeypair()
    print("System generated RSA key pair for both Person 1 and 2.")
    # Add signature with private keys generated from RSA key pair 
    # and public key input from user
    signed_pubkey1 = signMessage(private1, public_keyA)
    signed_pubkey2 = signMessage(private2, public_keyB)
    print("""Add signature process for Person 1 and 2 completed 
    with private key generated from combination of RSA key pair and theirs own public key\n""")
    
    # print("\nP1 signed message: ", signed_pubkey1) # Debbug line
    # print("\nP2 signed message: ", signed_pubkey2) # Debbug line

    ''' Eva Processing '''
    eva = int(input("Include Eva Processing? 0 for no, 1 for yes: "))
    if eva == 1:
        signed_pubkey1, signed_pubkey2 = manInMidWSign(public_keyA, public_keyB)

    # System check signature
    print("----------------------------------------------------")
    print("System start checking for signature with signed public key")
    print("----------------------------------------------------")
    if verifySignature(public1, str(public_keyA).encode(), signed_pubkey1):
        print("Person1's key is authenticated!")
    else:
        print("MitM detected! Connection aborted.")
        exit()  # Exit the system

    if verifySignature(public2, str(public_keyB).encode(), signed_pubkey2):
        print("Person2's key is authenticated!")
    else:
        print("MITM detected! Connection aborted.")
        exit()  # Exit the system
    
    print("\nKey Exchange Started...")
    secretA = keyGenerator(public_keyB, private_keyA, A)
    secretB = keyGenerator(public_keyA, private_keyB, A)
    print("Secure Shared Secret Person 1:", secretA)
    print("Secure Shared Secret Person 2:", secretB)

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
    print("----------------------------------------------------")
    print("\nSteps for man-in-the-middle-attack: ")
    print("----------------------------------------------------\n")
    print(f"2 prime public integers selected from both person are {A}, {B}\n")
    mainWithMitM(private_keyA, private_keyB, public_keyA, public_keyB, A, B)
    
    # Start MitM Protection
    print("----------------------------------------------------")
    print("MitM Protection")
    print("----------------------------------------------------\n")
    withPreventionProcess(private_keyA, private_keyB, public_keyA, public_keyB, A, B)
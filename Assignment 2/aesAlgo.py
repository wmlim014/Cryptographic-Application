from myInfo import *
from Task5.verify import *
from Task5.sign import *
from Task5.publickeyGen import writeFile
import sys

'''
Testing Example:
    `publickey.txt`
     - 5      # e1
     - 2983   # n1
     - 3      # e2
     - 12709  # n2

     Valid private key should be:
     - (d1, n1) = (1685, 2983)
     - (d2, n2) = (8307, 12709)
'''
if sys.argv[1] == "sign":
    myInfo("Task 5", [
            "1. AES Encryption & Decryption In Python: https://onboardbase.com/blog/aes-encryption-decryption/",
            """2. Ring Signature Theory: \t
            - chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://courses.csail.mit.edu/6.857/2020/projects/17-Barabonkov-Esteban-Fabrega.pdf \t
            - Lecture Note: LC - ring Signature.pdf""", 
            "3. Fast Exponentiation for Modular: https://www.geeksforgeeks.org/fast-exponentiation-in-python/"])
    
    # print(f"{readKeys()}\n\n{readMssage()}") # Debbug line
    user, private_key = requestPrivateKey()
    sign(user, private_key)

elif sys.argv[1] == "verify":
    isValid = verify()
    
    if isValid:
        print("True - Signature Verified!")
    else:
        print("False - Signature Verification Failed.")

elif sys.argv[1] == "gen": # Debbug line: 
    ''' Write publickey.txt and display the following:
        1. Valid private keys as: user-1; user-2
        2. value p, q and (p-1)(q-1)
        3. Public keys
    '''
    writeFile() 
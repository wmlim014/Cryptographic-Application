from myInfo import *
import hashlib
import random

class Hash:
    def __init__(self, x, m, h):
        self.x = x
        self.m = m
        self.h = h

def hexToBinConvertor(text):
    """ Using Naive Method in reference 2 """
    n = int(text, 16)
    bStr = '' 
    while n > 0: 
        bStr = str(n % 2) + bStr 
        n = n >> 1

    return bStr

def extractBits(text, start, end):
    first_str = text[:start] # Extract 1st N characters
    last_str = text[-end:] # Extract last N characters

    return first_str + last_str # Combine the extracted strings and return

def ssha1_hash(message):
    """ Compute the SSHA-1 hash and extract 34-bit hash (first 10 bits + last 24 bits). """
    full_hash = hashlib.sha1(message.encode()).hexdigest() # 160-bit hash in hexadecimal value
    binary_hash = hexToBinConvertor(full_hash)  # Convert full_hash value to binary value
    # print("Full binary hash: ", binary_hash)  # Debbug line
    
    extracted_hash = extractBits(binary_hash, 10, 24)
    # print("Extracted binary hash: ", extracted_hash)  # Debbug line
    return extracted_hash

    
def messageForHash(min_x, max_x, x=0):
    """ Generating message for hashing """
    myFirstName = "Wen Mi"
    x = random.randint(min_x, max_x) # Initialize an x value H(m) generation
    m = f"Mario owes {myFirstName} {x} dollars" # Initialize message m

    return x, m

def findCollision(min_x, max_x):
    hash_table = {} # Dictionary to store all hashed values
    trial = 0
    print("Finding collision integer pair...")
    while True:
        trial += 1

        x, m = messageForHash(min_x, max_x) # Find message
        h = ssha1_hash(m)

        """ In collision, H(m) = H(m') but m != m' """
        if h in hash_table: # Collision found
            for existing_entry in hash_table[h]:
                if existing_entry.x != x: # Where x != x'
                    return existing_entry, Hash(x, m, h), trial
        
        # Store the hash value as a list, 
        # so that we can check if the hash value generated before
        hash_table[h] = []  # Initialize empty list if not exists
        hash_table[h].append(Hash(x, m, h))

        # Print progress every 100,000 trials
        if trial % 100000 == 0:
            print(f"Trials: {trial}, Hashes stored: {len(hash_table)}")

def displayInfo():
    r1 = "https://www.geeksforgeeks.org/sha-in-python/"
    r2 = "https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/"
    r3_1 = "https://www.geeksforgeeks.org/python-first-n-letters-string-construction/"
    r3_2 = "https://www.geeksforgeeks.org/python-get-last-n-characters-of-a-string/"

    myInfo("Task 4", [
        f"1. SHA in Python: {r1}", 
        f"2. Convert hex into binary: {r2}",
        f"3. Extract N characters of string: \n\t{r3_1}\n\t{r3_2}"])
    
def getIndex(li, target): 
    for index, x in enumerate(li): 
        if x.h == target: 
            return index 
    return -1

if __name__ == '__main__':
    
    displayInfo()
    """ Tested with the following:
        message = Mario owes Wen Mi 5 dollars
        expected extracted binary hash = 1101101101100101110011000010100100
        actual extracted binary hash   = 1101101101100101110011000010100100
        Compared the expected and actual extracted hash with:
        https://www.maxai.co/text-tools/text-compare/?ref=googleads&gad_source=1&gclid=CjwKCAiA2cu9BhBhEiwAft6IxJnNd-KA5Cxl0Kzkq6lvpFt3QOao_A_TnM0hwcB9krneqP3d1qgX2xoCmzwQAvD_BwE
    """
    # Set minimum and maximum x for generate the x value randomly
    # the larger range increase the larger probability to find the integer pair (x, x')
    min_x, max_x = 1, 10**6  
    existing_entry, new_entry, trial = findCollision(min_x, max_x)

    print("Message 1: ", existing_entry.m)
    print("Message 2: ", new_entry.m)

    print("Hashed Value for Message 1: ", existing_entry.h)
    print("Hashed Value for Message 2: ", new_entry.h)

    print(f"Number of trial to find the integer pair ({existing_entry.x}, {new_entry.x}) for collision: {trial}")
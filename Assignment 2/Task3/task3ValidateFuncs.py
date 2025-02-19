'''
    This file is for task 3 validats functions
'''

def isSuperIncreasing(private_keys):
    '''
        Check if the private key is super increasing
        a(i) => private key(i) + total
    '''
    total = 0
    for curr_pk in private_keys:
        if curr_pk <= total:
            print("The entered sequence is not super-increasing. \nExiting...")
            exit()
        total += curr_pk
    return total

def validateModular(m, mod, private_keys):
    ''' Check if the multiplier satisfied:
        1. The value of mod must be greatest than the sum of all private key value
        2. The value of (m) should have no common factor with mod
        Example: multiplier(m) = 3, mod = 7
            In range --> x(i) = {0, 1, 2, ..., 6}:
            (m * x(i)) modulus mod must return 1
                else, the multiplier is unsatisfied
    '''
    if isSuperIncreasing(private_keys) > mod:
        print("Invalid modulus value. The modulus value must be greatest than the sum of all private key value")
        print("Existing...")
        exit()

    # Valudate Multiplier
    for i in range(0, mod - 1):
        if (m * i) % mod == 1:
            return i
    
    print("Multiplier condition is not satisfied. The multiplier should have no common factor with modulus value")
    print("Exiting...")
    exit()

def validatePlainText(size, plaintexts):

    if len(plaintexts) == size: 
        for p in plaintexts:
            if p not in (0, 1):
                print("Invalid binary message, a binary message should contain only 0 and 1.")
                print("Existing...")
                exit()
    else:
        print(f"Invalid binary message, the length of the binary message must be {size}")
        print("Existing...")
        exit()
from myInfo import *

# Recursive function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a, b, gcd):
    return (a * b // gcd)

# Main function
if __name__ == '__main__':
    myInfo("Task 1", 
           ["1. Program to find LCM of two numbers: https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/"])
    
    # Main process
    a = int(input("Enter whole integer 'a': "))
    b = int(input("Enter whole integer 'b': "))

    print(f"\nComputing LCM({a}, {b}) with GCD({a}, {b})...")
    # Return gcd(a, b)
    computed_gcd = gcd(a, b)
    print(f"GCD({a}, {b}) is: {computed_gcd}")
    print(f"LCM({a}, {b}) is: ", lcm(a, b, computed_gcd))
from myInfo import *
from texttable  import Texttable

class GCDs:
    def __init__(self, a, b, q, r):
        self.a = a
        self.b = b
        self.q = q
        self.r = r

    def __str__(self):
        return f'Attributes: {self.__dict__}'

def createTable():
    t = Texttable() # Initialize texttable to display the result for each row later
    t.header(['n1', 'n2', 'r', 'q', 'a1', 'b1', 'a2', 'b2']) # Add header

    return t

def addTableRow(n1, n2, r, q, a1, b1, a2, b2, t):
    t.add_row([n1, n2, r, q, a1, b1, a2, b2])

    return t


def gcd(a, b):
    '''
        Example:
        1. Basic Euclidean Algorithm, `a = qb + r`
            Given: gcd(a, b) = gcd(39, 11)
                39 = (3)11 + 6    --> q=3, r=6
                11 = (1)6 + 5     --> q=1, r=5
                6 = (1)5 + 1      --> q=1, r=1
                5 = (5)1 + 0      --> q=5, r=0
            Hence, gcd(39, 11) = gcd(11, 6) = gcd(6, 5) = gcd(5, 1) = gcd(1, 0) = 1
            ** Where the basic Euclidean Algorithm stop when r = 0 **
    '''
    # Make sure a is always larger than b
    if (a < b):
        temp_a = a
        a = b
        b = temp_a
    
    q = a//b # Return truncated integer part of a number (Not round up or down)
    r = a - (q*b)

    return a, b, q, r

def getGcdLists(a, b):
    gcd_list = []

    # Start gcd compulation
    while b != 0:
        a, b, q, r = gcd(a, b)
        gcd_list.append(GCDs(a, b, q, r))
        # Update gcd(a, b) to gcd(b, r)
        a = b
        b = r

    return gcd_list, a, b

def gcdExtended(a, b, t):
    '''
        Example After Basic Euclidean Algorithm:
        2. Observe:
            39 = (1)39 + (0)11  --> a1 = 1, b1 = 0, n1 = 39, n2 = 11
            11 = (0)39 + (1)11  --> a2 = 0, b2 = 1, n1 = 39, n2 = 11

            --> a1 = 1, b1 = 0, a2 = 0, b2 = 1, n1 = 39, n2 = 11
            6 = (1 - (3)(0))39 + (0 - (3)(1))11 = (1)39 + (-3)11

            --> a1 = 0, b1 = 1, a2 = 1, b2 = -3, n1 = 11, n2 = 6
            5 = (0 - (1)(1))39 + (1 - (1)(-3))11 = (-1)39 + (4)11
    '''
    gcd_list, a, b = getGcdLists(a, b)
    final_gcd = gcd_list[len(gcd_list) - 1].a

    # Initialize base case
    a1, b1 = 1, 0
    a2, b2 = 0, 1
    addTableRow(gcd_list[0].a, gcd_list[0].b, gcd_list[0].r, gcd_list[0].q, a1, b1, a2, b2, t)
    n1 = gcd_list[0].a
    n2 = gcd_list[0].b

    for i in range(0, len(gcd_list) - 1):
        # Compute new coefficients
        x = n1 // n2
        a3 = a1 - (x * a2)
        b3 = b1 - (x * b2)
        n3 = n1 - (x * n2)

        # Update new coeficients
        a1, b1 = a2, b2
        a2, b2 = a3, b3
        n1, n2 = n2, n3
        
        addTableRow(n1, n2, gcd_list[i].r, gcd_list[i].q, a1, b1, a2, b2, t)
        # print(f"{gcd_list[index].a} = {gcd_list[index].q}({gcd_list[index].b}) + {gcd_list[index].r}")  # Debbug line

    return final_gcd, a2, b2

# Main function
if __name__ == '__main__':
    myInfo("Task 2", [
            "1. Euclidean algorithms (Basic and Extended): https://github.com/ImperialCollegeLondon/Mathematical-Computing-Demo/blob/master/M1C%20(Python)/M1C-Number-Theory/.ipynb_checkpoints/Python%20Number%20Theory%2003%20-%20Extended%20Euclidean%20Algorithm-checkpoint.ipynb", 
            "2. Printing Lists as Tabular Data in Python: https://www.geeksforgeeks.org/printing-lists-as-tabular-data-in-python/"])
    
    # Main process
    # Get a & b from user input
    a = int(input("Enter whole integer 'a': "))
    b = int(input("Enter whole integer 'b': "))

    # Process to return the output for each row in
    t = createTable()
    final_gcd, a2, b2 = gcdExtended(a, b, t)
    
    print(f"\nWe are to find gcd({a}, {b}) using the Extended Eucledian Algorithm.")
    print("The contents of the variables are as follows: ")
    print(t.draw())

    print(f"\nSummary: \ngcd({a}, {b}) = {final_gcd}")
    print(f"({a} * {a2}) + ({b} * {b2}) = {final_gcd}")

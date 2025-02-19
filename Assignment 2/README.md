# Student Information
> NAME: Lim Wen Mi
> STUDENT ID: 7894363
> Submission for: CSCI361 - Assignment 2

[!NOTE]
> Before the implementation, do remember redirect the file path to this folder. :innocent:
> This submissions had been generated in python 3 environment.

# Implementation
## Task 1
```
python Task1.py
```

## Task 2
[!IMPORTANT]
> Install texttable library
> ```
> pip install texttable
> ```

Implementation
```
python Task2.py
```

## Task 3
```
python knapsack.py
```
[!NOTE]
> All validate functions for task 3 are allocated in `Task3/task3ValidateFuncs.py`

## Task 4
```
python ssha1.py
```

## Task 5
[!IMPORTANT]
> Install Crypto library
> ```
> pip install pycryptodome
> pip install --force-reinstall pycryptodome
> ```

### Compile sign.py
*The `publickey.txt` and `message.txt` must located in: `Task5`*
*The `signature.txt` will generated in: `Task5`*
```
python aesAlgo.py sign
```

### Compile verify.py
```
python aesAlgo.py verify
```

Addition notes: 
- To generate the public key and compute the valid private key
```
python aesAlgo.py gen
```
*p and q generated with `sympy.randprime` to make sure they are prime in range 0 to 200*

## Task 6
```
python Task6.py
```

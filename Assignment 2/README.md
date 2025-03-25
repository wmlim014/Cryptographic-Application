# Student Information
> NAME: Lim Wen Mi

> STUDENT ID: 7894363

> Submission for: CSCI361 - Assignment 2

> GitHub: [Assignment 2](https://github.com/wmlim014/Cryptographic-Application/tree/main/Assignment%202)

> [!NOTE]
> Before the implementation, do remember redirect the file path to this folder. :innocent:
> This submissions had been generated in python 3.12.5 environment.

# Implementation
## Task 1
```
python Task1.py
```

## Task 2
> [!IMPORTANT]
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
> [!NOTE]
> All validate functions for task 3 are allocated in `Task3/task3ValidateFuncs.py`

## Task 4
```
python ssha1.py
```

## Task 5
> [!IMPORTANT]
> Install Sympy and Crypto library
> ```
> pip install sympy
> pip install pycryptodome
> pip install --force-reinstall pycryptodome
> ```

Addition notes: 
- To import the `publickey.txt` and `message.txt` files, please allocate in folder called `Task5`
- To generate the `publickey.txt` and compute the valid private key
```
python aesAlgo.py gen
```
*p and q generated with `sympy.randprime` to make sure they are prime in range 0 to 200*

### Compile sign.py - Generate `signature.py`
*The `signature.txt` will generated in: `Task5/sign.py`
```
python aesAlgo.py sign
```

### Compile verify.py - Verify `signature.py`
```
python aesAlgo.py verify
```

## Task 6
> [!NOTE]
> In Man in the Middle attack (MitM) protection, enter:
> - 1 for include MitM
> - 0 for not include MitM
> to check is the Signature checking work
```
python Task6Main.py
```
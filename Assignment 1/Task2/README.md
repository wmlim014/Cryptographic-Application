> [!NOTE]
> 1. Please replace `[*]` with your own parameters
> 2. Execute with Java 8 or above and in Window version
> 3. Special characters will not be encrypted
> 4. ![GitHub Link](https://github.com/wmlim014/Cryptographic-Application/tree/main/Assignment%201/Task2)

# Executions
```
cd [YouStorageLocation]/7894363_LimWenMi/Task2
javac GenerateCipher.java FileProcessor.java SubstitutionCipher.java
```

## Encryption
```
java SubstitutionCipher encrypt --keyword [KEYWORD] --input [INPUT_PATH] --output [OUTPUT_PATH]
```

## Decryption
```
java SubstitutionCipher decrypt --keyword [KEYWORD] --input [INPUT_PATH] --output [OUTPUT_PATH]
```

# Error Handling
1.  Prevent user input encryption key with special characters (non-alphabets symbol)
2.	File not found exception
3.	Prevent user provide invalid encrypt/decrypt mode (e.g. user not allowed to fill encrypt/decrypt with other word)
4.	Prevent user input plaintext file with digits
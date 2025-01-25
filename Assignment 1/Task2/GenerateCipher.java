     /********************************************************/
    /*   NAME       : Lim Wen Mi                            */
   /*    FILE NAME  : GenerateCipher.java                  */
  /*     SUBMISSION : Assignment 1 Task 2                 */
 /*      DESCRIPTION: I declare that this is my own work */
/********************************************************/

import java.util.*;

public class GenerateCipher {

    private static final String CHARACTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";  // Set A-Z as default list
    private final String cipherChar;

    // Default Constructor
    public GenerateCipher (String key) {
        this.cipherChar = generateCipherChar(key);
    }

    // Encryption function
    public Map<Character, Character> getEncryptionMap() {
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < CHARACTER.length(); i++) {
            map.put(CHARACTER.charAt(i), cipherChar.charAt(i));
        }
        return map;
    }

    // Decryption function
    public Map<Character, Character> getDecryptionMap() {
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < cipherChar.length(); i++) {
            map.put(cipherChar.charAt(i), CHARACTER.charAt(i));
        }
        return map;
    }

    // Remove the duplicate charaters from keyword
    private String removeDuplicatesChar (String key){
        // If the keyword contain non-CHARACTER characters
        if(!key.matches("[A-Za-z]+")) 
            throw new IllegalArgumentException("Keyword should contain CHARACTER only.");

        // Set prevent duplicate items added into element
        LinkedHashSet<Character> set = new LinkedHashSet<>();
        for (char c: key.toUpperCase().toCharArray()){
            set.add(c);
        }
        return convertListToString(new ArrayList<>(set));
    }

    // Convert split string in list back to a string
    private String convertListToString(List<Character> list) {
        StringBuilder sb = new StringBuilder();
        for (Character c: list) {
            sb.append(c);
        }
        return sb.toString();
    }

    private String generateCipherChar (String key){
        String preprocessKey = removeDuplicatesChar(key);
        
        // Get CHARACTER never used
        List<Character> remainingChar = new ArrayList<>();
        for(char c: CHARACTER.toCharArray()){ // For each character in default A-Z list
            // If not included in the keyword
            if (preprocessKey.indexOf(c) == -1)
                remainingChar.add(c);
        }

        // Rever all un-used characters
        Collections.reverse(remainingChar);
        // Combine keyword and un-used character
        String cipher = preprocessKey + convertListToString(remainingChar); 

        // Check if the ciphertext generated correctly
        if (cipher.length() != 26) 
            throw new IllegalArgumentException("Invalid cipher CHARACTER generated.");

        return cipher;
    }
}
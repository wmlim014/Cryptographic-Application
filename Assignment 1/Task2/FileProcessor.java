     /********************************************************/
    /*   NAME       : Lim Wen Mi                            */
   /*    FILE NAME  : FileProcessor.java                   */
  /*     SUBMISSION : Assignment 1 Task 2                 */
 /*      DESCRIPTION: I declare that this is my own work */
/********************************************************/

import java.io.*;
import java.util.Map;

public class FileProcessor {
    
    // Default constructor
    public static void processFile(String inputPath, String outputPath, 
                                    Map<Character, Character> transformationMap) throws
    
    IOException {
        // Try to read input file path and write an output file path
        try (BufferedReader  input = new BufferedReader(new FileReader (inputPath));
             BufferedWriter  output = new BufferedWriter(new FileWriter (outputPath)))
        {
            String line;
            while ((line = input.readLine()) != null){ // While current line is not empty
                // Convert current line into uppercase and process it
                String processedLine = processLine(inputPath, line.toUpperCase(), transformationMap);
                // Write current line
                output.write(processedLine);
                output.newLine();
            }
        }
    }

    // Processing current input file line
    private static String processLine(String inputPath, String line, Map<Character, Character> transformationMap) {
        StringBuilder sb = new StringBuilder();
        for (char c: line.toCharArray()){ // For each character in this line...
            if (Character.isDigit(c)) // If current line contains digits
                throw new IllegalArgumentException(inputPath + " should not contains digits.");

            if(!Character.isLetter(c)){ // If current character is not a letter...
                // throw new IllegalArgumentException(inputPath + " contain non-alphabetic characters: " + c);
                sb.append(c); // Preserve original character (space, special characters, etc.)
                continue;
            }
            
            // If no non-alphabet in this line...
            Character transformed = transformationMap.get(c);
            if (transformed == null)
                throw new IllegalArgumentException("Unable to encrypt due to no mapping found: " + c);
            
            sb.append(transformed);
        }
        return sb.toString(); // Return current line
    }
}
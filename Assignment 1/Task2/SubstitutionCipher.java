     /********************************************************/
    /*   NAME       : Lim Wen Mi                            */
   /*    FILE NAME  : SubstitutionCipher.java              */
  /*     SUBMISSION : Assignment 1 Task 2                 */
 /*      DESCRIPTION: I declare that this is my own work */
/********************************************************/

import java.util.Map;
import java.io.IOException;

public class SubstitutionCipher {

    private static final String COMMAND_LINE = "java SubstitutionCipher [encrypt|decrypt] --keyword <KEYWORD> --input <INPUT_FILE_PATH> --output <OUTPUT_FILE_PATH>";
    // Declare arguments files
    private static class Arguments {
        String mode;
        String keyword;
        String inputFile;
        String outputFile;
    }

    // Allocate arguments
    private static Arguments parseArguments(String[] args){
        Arguments arguments = new Arguments();

        try{
            arguments.mode = args[0];
            for (int i = 1; i < args.length; i++) {
                // Allocate the arguments passed into arguments class
                switch (args[i]) {
                    case "--keyword":
                        arguments.keyword = args[++i];
                        break;
                    case "--input":
                        arguments.inputFile = args[++i];
                        break;
                    case "--output":
                        arguments.outputFile = args[++i];
                        break;
                }
            }
        } catch (IndexOutOfBoundsException e) { // Error Catch if unexpected argument passed
            throw new IllegalArgumentException("Invalid arguments format");
        }
        
        validateArguments(arguments);
        return arguments;
    }

    // Arguments Validation
    // Check is encrypt / decrypt mode passed in arguments (is collect mode passed)
    // Check is the arguments empty
    private static void validateArguments(Arguments arguments){
        if (!arguments.mode.matches("encrypt|decrypt")) // If the argument mode is not passed as encrypt or decrypt...
            throw new IllegalArgumentException("Invalid mode. Use 'encrypt or decrypt'");

        if (arguments.keyword == null || arguments.inputFile == null 
            || arguments.outputFile == null) // If the allocated argument is empty...
            throw new IllegalArgumentException("Missing required arguments\nUsage: " + COMMAND_LINE);
    }

    public static void main(String[] args){
        try {
            Arguments arguments = parseArguments(args);
            GenerateCipher generateCipher = new GenerateCipher(arguments.keyword);

            // Proceed to encrypt or decrypt from input
            Map<Character, Character> transformationMap;
            if (arguments.mode.equals("encrypt"))
                transformationMap = generateCipher.getEncryptionMap();
            else
                transformationMap = generateCipher.getDecryptionMap();

            // Proceed to process input and output file
            FileProcessor.processFile(arguments.inputFile, arguments.outputFile, transformationMap);
            System.out.println(arguments.mode + " operation completed successfully.");
        } catch (IllegalArgumentException | IOException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }
}
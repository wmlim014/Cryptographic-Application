# myInfo.py

# Display my student information
def myInfo(submissionFor, references = []):
    print("Name: Lim Wen Mi")
    print("Student ID: 7894363")
    print(f"Submission for: CSCI361-A2 ~ {submissionFor}")
    print("Declaration: I declare that this submission is my own work.")

    # Print references
    if len(references) > 0:
        print("\nReference: ")
        for r in references:
            print(f"{r}")

    print("\n---------------------------------------------------------------------------------------\n")
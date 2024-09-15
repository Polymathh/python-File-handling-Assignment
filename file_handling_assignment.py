# File handling with error handling
try:
    # File Creation: Create a new text file in write mode and write three lines of text
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("The number of students in the class is 25.\n")
        file.write("Python is a powerful programming language.\n")
    print("File created and initial text written successfully.")

    # File Reading: Read and display the contents of the file
    with open("my_file.txt", "r") as file:
        print("\nReading the contents of 'my_file.txt':")
        content = file.read()
        print(content)

    # File Appending: Open the file in append mode and add three additional lines
    with open("my_file.txt", "a") as file:
        file.write("Adding an extra line to the file.\n")
        file.write("Here is a random number: 42.\n")
        file.write("Goodbye!\n")
    print("Additional lines appended successfully.")

    # Read the updated content and display
    with open("my_file.txt", "r") as file:
        print("\nReading the updated contents of 'my_file.txt':")
        updated_content = file.read()
        print(updated_content)

# Error Handling: Handle potential file-related exceptions
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile operation complete.")


# handling.py
# Week 4 Assignment: File Handling & Error Handling in Python

def modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as f:
            content = f.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_file, 'w') as f:
            f.write(modified_content)

        print(f"✅ File '{input_file}' has been read and '{output_file}' has been created successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{input_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ask the user for a filename
    filename = input("Enter the filename to read (e.g., input.txt): ").strip()
    output_filename = "output.txt"

    # Call the function
    modify_file(filename, output_filename)



def create_and_write_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: This is the first line.\n")
            file.write("Line 2: Here's a number: 42\n")
            file.write("Line 3: And another line with more text.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_and_display_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Line 4: Appending new content.\n")
            file.write("Line 5: Another appended line.\n")
            file.write("Line 6: Yet another line appended.\n")
        print("Additional lines appended successfully.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()

# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line here.\n")
        print("File 'my_file.txt' created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nContents of 'my_file.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to access 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1.\n")
        file.write("67890\n")
        file.write("Yet another line appended.\n")
        print("\nThree additional lines appended to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("Task completed.")

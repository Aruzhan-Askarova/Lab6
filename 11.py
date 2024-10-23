import string

# Generate file names from A to Z
for letter in string.ascii_uppercase:
    # Open the file for writing (creates the file if it doesn't exist)
    with open(f"{letter}.txt", "w") as file:
        # Optionally, you can write something to each file
        file.write(f"This is the file for {letter}\n")

print("Files A.txt to Z.txt have been created.")

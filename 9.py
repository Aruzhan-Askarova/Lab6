def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 0

# Example usage
file_path = input("Enter the file path: ")
line_count = count_lines_in_file(file_path)
print(f"Number of lines in the file: {line_count}")

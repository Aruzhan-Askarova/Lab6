import os

def delete_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return

    # Check if the file is accessible (read/write permissions)
    if not os.access(file_path, os.W_OK):
        print(f"Error: You do not have permission to delete {file_path}.")
        return

    try:
        # Delete the file
        os.remove(file_path)
        print(f"File {file_path} has been successfully deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_to_delete = "example.txt"
delete_file(file_to_delete)

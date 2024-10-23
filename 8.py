import os

def check_path_info(path):
    # Check if the path exists
    if os.path.exists(path):
        # Get the directory portion of the path
        directory = os.path.dirname(path)
        # Get the file name portion of the path
        filename = os.path.basename(path)
        
        print(f"Path exists: {path}")
        print(f"Directory portion: {directory}")
        print(f"Filename portion: {filename}")
    else:
        print(f"Path does not exist: {path}")

# Example usage
path = input("Enter the path to check: ")
check_path_info(path)

import os

def check_access(path):
    # Check if the path exists
    exists = os.path.exists(path)
    
    # Check if the path is readable
    readable = os.access(path, os.R_OK)
    
    # Check if the path is writable
    writable = os.access(path, os.W_OK)
    
    # Check if the path is executable
    executable = os.access(path, os.X_OK)

    return exists, readable, writable, executable

# Example usage
path = input("Enter the path to check: ")

exists, readable, writable, executable = check_access(path)

print(f"Path: {path}")
print(f"Exists: {exists}")
print(f"Readable: {readable}")
print(f"Writable: {writable}")
print(f"Executable: {executable}")

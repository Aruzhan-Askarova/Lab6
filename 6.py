import os

def list_directories(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

def list_files(path):
    return [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]

def list_all(path):
    return os.listdir(path)

# Example usage
path = '.'  # Specify the path here

directories = list_directories(path)
files = list_files(path)
all_items = list_all(path)

print(f"Directories in {path}: {directories}")
print(f"Files in {path}: {files}")
print(f"All items in {path}: {all_items}")

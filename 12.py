def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode and destination file in write mode
        with open(source_file, "r") as src, open(destination_file, "w") as dest:
            # Read the contents of the source file and write it to the destination file
            dest.write(src.read())
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source = "source.txt"
destination = "destination.txt"
copy_file(source, destination)

def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List written to file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data = ['apple', 'banana', 'cherry', 'date']
file_path = 'fruits.txt'

write_list_to_file(file_path, data)

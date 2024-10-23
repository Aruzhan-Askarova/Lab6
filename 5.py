def check_all_true(input_tuple):
    return all(input_tuple)

# Example usage
example_tuple = (True, 1, 'non-empty string', 3.14)  # All values are considered true
result = check_all_true(example_tuple)
print(f"All elements are true: {result}")

from functools import reduce

def multiply_list(numbers):
    # Use reduce with a lambda function to multiply all the numbers in the list
    return reduce(lambda x, y: x * y, numbers)

# Example usage
numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(f"Multiplication of all numbers in the list: {result}")


def is_palindrome(s):
    # Remove spaces and convert the string to lowercase for a case-insensitive comparison
    cleaned_string = ''.join(filter(str.isalnum, s)).lower()
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

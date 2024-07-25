def analyze_string(s):
    has_alphanumeric = any(c.isalnum() for c in s)
    has_alphabetical = any(c.isalpha() for c in s)
    has_digits = any(c.isdigit() for c in s)
    has_lowercase = any(c.islower() for c in s)
    has_uppercase = any(c.isupper() for c in s)

    return has_alphanumeric, has_alphabetical, has_digits, has_lowercase, has_uppercase

# Example usage:
user_string = input("Enter a string: ")
alphanumeric, alphabetical, digits, lowercase, uppercase = analyze_string(user_string)

print(f"Alphanumeric characters present: {alphanumeric}")
print(f"Alphabetical characters present: {alphabetical}")
print(f"Digits present: {digits}")
print(f"Lowercase characters present: {lowercase}")
print(f"Uppercase characters present: {uppercase}")

def transform_string(input_string):
    # Split the string on spaces and join using hyphens
    return "-".join(input_string.split())

# Example usage:
original_string = "Hello World! This is Copilot."
transformed_string = transform_string(original_string)
print(transformed_string)  # Output: Hello-World!-This-is-Copilot.

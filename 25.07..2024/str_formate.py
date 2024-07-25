def print_integer_formats(n):
    print(f"Decimal: {n}")
    print(f"Octal: {oct(n)[2:]}")  # Remove the '0o' prefix
    print(f"Hexadecimal: {hex(n)[2:].upper()}")  # Remove the '0x' prefix and capitalize
    print(f"Binary: {bin(n)[2:]}")  # Remove the '0b' prefix

# Example usage:
user_input = int(input("Enter an integer: "))
print_integer_formats(user_input)

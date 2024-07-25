def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Oops! You tried to divide by zero.")
        return None

# Example usage:
numerator = 10
denominator = 0

result = divide(numerator, denominator)
if result is not None:
    print(f"Result: {result}")
else:
    print("Division failed.")

print("Continuing with the rest of the program...")

def is_leap(year):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

# Example usage:
year1 = 2020
print(is_leap(year1))  # Output: True (2020 is a leap year)

year2 = 2021
print(is_leap(year2))  # Output: False (2021 is not a leap year)

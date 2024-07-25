def count_substring_occurrences(main_string, substring):
    count = 0
    start_index = 0

    while True:
        index = main_string.find(substring, start_index)
        if index == -1:
            break 
        count += 1
        start_index = index + 1  

    return count

# Example usage:
user_string = input("Enter the main string: ")
user_substring = input("Enter the substring to search for: ")

result = count_substring_occurrences(user_string, user_substring)
print(f"The substring '{user_substring}' appears {result} times in the given string.")

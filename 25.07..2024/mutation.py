def modify_immutable_string(original_string, new_suffix):
  
    modified_string = original_string + new_suffix
    return modified_string

# Example usage:
immutable_string = "Hello, Immutable World!"
new_suffix = " (with a twist)"
result = modify_immutable_string(immutable_string, new_suffix)
print(result) 

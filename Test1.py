import re

# Define the regular expression pattern
pattern = r"^[^a-z]*$"

# Function to check if a string matches the pattern
def check_string(input_string):
    if re.match(pattern, input_string):
        print(f"'{input_string}' matches the pattern!")
    else:
        print(f"'{input_string}' does NOT match the pattern.")

# Test cases
test_strings = [
    "123456",         # Match
    "HELLO",          # Match
    "!@#$%^&*()",     # Match
    "123 ABC",        # Match
    "*&&^%$#",        # Match
    "hello",          # Does NOT match
    "abc123",         # Does NOT match
    "LowerCase1",     # Does NOT match
    "NoLower123!"     # Match
]

# Check each test string
for test_str in test_strings:
    check_string(test_str)

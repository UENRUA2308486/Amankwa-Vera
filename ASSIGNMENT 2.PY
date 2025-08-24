#'Task 1: Convert Uppercase to Lowercase'
def to_lowercase(s):
    return s.lower()
# Example usage
print(to_lowercase("Hello"))  # Output: "hello"


#Task 2: Swap Case of Letters
def swap_case(s):
    return s.swapcase()
# Example usage
print(swap_case("HeLLo WoRLd"))  # Output: "hEllO wOrlD"


#Task 3: Remove Uppercase Letters
def remove_uppercase(s):
    return ''.join([char for char in s if not char.isupper()])
# Example usage
print(remove_uppercase("HelloWorld"))  # Output: "elloorld"

#Task 4: Count Uppercase and Lowercase Letters
def count_case(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    return f"Uppercase: {uppercase_count}, Lowercase: {lowercase_count}"
# Example usage
print(count_case("EngiNEEr"))  # Output: "Uppercase: 4, Lowercase: 4"


#'Task 5: Remove Non-English Letters'

def remove_non_english(s):
    return sum(r'[^a-zA-Z]', '', s)
# Example usage
print(remove_non_english("Data - Driven@2025!")) 
# Output: "DataDriven"


#'Task 6: Calculate Area of Triangle using Heron’s Formula'
import math

def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
# Example usage
print(heron_area(3, 4, 5))  # Output: 6.0


#'Task 7: Format Names in a Table'
def format_names(names):
    for name in names:
        print(name.ljust(20), name.rjust(20))
# Example usage
format_names(["Alice", "Bob", "Charlie"])


#'Task 8: Clean a String'
import string

def clean_string(s):
    return ''.join(s.strip().translate(str.maketrans('', '', string.punctuation)).split())
# Example usage
print(clean_string("   Hello, World!   "))  # Output: "HelloWorld"

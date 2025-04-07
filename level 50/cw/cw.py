#1st codewars: 
def str_count(s, char):
    return s.count(char)

print(str_count("hello", 'l'))  # Output: 2
print(str_count("Hello", 'o'))  # Output: 1
print(str_count("", 'z'))       # Output: 0


#2nd codewars
def is_even(n):
    # If the number is a float with a non-zero decimal part, return False
    if isinstance(n, float) and n % 1 != 0:
        return False
    # Check if the number is divisible by 2
    return n % 2 == 0
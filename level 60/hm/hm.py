#first codewars:
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)



#second codewars:
def reverse_seq(n):
    return list(range(n, 0, -1))



#third codewars
def is_isogram(string):
    string = string.lower()  # Convert string to lowercase
    seen = set()  # Set to store the characters we've encountered
    
    for char in string:
        if char in seen:
            return False  # If the character is already in the set, it's not an isogram
        seen.add(char)  # Add the character to the set
    
    return True  # If no duplicates were found, it's an isogram

#1st codewars
def reverse_words(s):
    # Split the string into words (keeping multiple spaces intact)
    words = s.split(' ')  # This will keep the spaces intact
    
    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back into a single string with spaces
    return ' '.join(reversed_words)

# Test cases
print(reverse_words("This is an example!"))  
print(reverse_words("double  spaces"))     

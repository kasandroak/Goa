#1st codewars
def boolean_to_string(b):
    return str(b)


#2nd codewars
def is_even(n):
    # If the number is a float with a non-zero decimal part, return False
    if isinstance(n, float) and n % 1 != 0:
        return False
    # Check if the number is divisible by 2
    return n % 2 == 0


#3rd codewars
def make_negative(n):
    # If n is already negative, return n. Otherwise, return -n
    return -abs(n)


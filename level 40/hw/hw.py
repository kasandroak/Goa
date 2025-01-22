#1st codewars
def reverse(lst):
    reversed_list = list()
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list



#2nd codewars
def initialize_names(name):
    name_parts = name.split()  # Split the name into parts (first, middle, last)
    
    if len(name_parts) > 2:  # Check if there's a middle name
        # Convert middle names to their initials (first letter + '.')
        name_parts = [name_parts[0]] + [part[0] + '.' for part in name_parts[1:-1]] + [name_parts[-1]]
    
    # Join the name parts back into a single string and return
    return ' '.join(name_parts)


#3rd codewars
def add(a, b):
    # Convert both numbers to strings
    a_str = str(a)
    b_str = str(b)
    
    # Pad the shorter string with leading zeros
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    # Initialize an empty result
    result = ""
    
    # Add the digits from left to right without carrying over
    for i in range(max_len):
        # Add the corresponding digits and store the result
        sum_digits = int(a_str[i]) + int(b_str[i])
        result += str(sum_digits)
    
    # Return the final result as an integer
    return int(result)

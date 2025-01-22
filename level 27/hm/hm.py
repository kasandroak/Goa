# 1. Demonstrate string functions
text = "Hello World!"

# .upper() - Converts all characters in the string to uppercase
print(text.upper())  # Output: HELLO WORLD!

# .lower() - Converts all characters in the string to lowercase
print(text.lower())  # Output: hello world!

# .capitalize() - Capitalizes the first character of the string
print(text.capitalize())  # Output: Hello world!

# .swapcase() - Swaps the case of all characters in the string
print(text.swapcase())  # Output: hELLO wORLD!

# .find() - Finds the first occurrence of the specified value and returns its index; returns -1 if not found
print(text.find("World"))  # Output: 6

# len() - Returns the number of characters in the string
print(len(text))  # Output: 12

# 2. Demonstrate list functions
my_list = [1, 2, 3, 4, 5]

# .append() - Adds an element to the end of the list
my_list.append(6)  # my_list becomes [1, 2, 3, 4, 5, 6]
print(my_list)

# .insert() - Inserts an element at a specified position in the list
my_list.insert(2, 10)  # Inserts 10 at index 2; my_list becomes [1, 2, 10, 3, 4, 5, 6]
print(my_list)

# .pop() - Removes and returns the element at the specified position (last element if no position is specified)
removed_element = my_list.pop()  # Removes 6; my_list becomes [1, 2, 10, 3, 4, 5]
print(removed_element)  # Output: 6
print(my_list)

# Example of .pop() with index
removed_element = my_list.pop(2)  # Removes element at index 2 (which is 10); my_list becomes [1, 2, 3, 4, 5]
print(removed_element)  # Output: 10
print(my_list)
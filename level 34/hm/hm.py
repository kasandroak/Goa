# Classwork 2: Basic List Operations
print("Classwork 2: Basic List Operations")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruits)

# Access and print the first and last items
first_item = fruits[0]
last_item = fruits[-1]
print("First item:", first_item)
print("Last item:", last_item)

# Add a new fruit "fig" to the list
fruits.append("fig")
print("List after adding 'fig':", fruits)

# Remove "banana" from the list
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Change the value of the second item to "blueberry"
fruits[1] = "blueberry"
print("List after changing the second item to 'blueberry':", fruits)

# Print the length of the list
print("Length of the list:", len(fruits))

print("\nClasswork 3: List Functions and Methods")
# Classwork 3: List Functions and Methods
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Append 100
numbers.append(100)
print("After appending 100:", numbers)

# Insert 5 at the beginning
numbers.insert(0, 5)
print("After inserting 5 at the beginning:", numbers)

# Remove 30
numbers.remove(30)
print("After removing 30:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Reverse the list
numbers.reverse()
print("After reversing:", numbers)

# Find index of 50
index_of_50 = numbers.index(50)
print("Index of 50:", index_of_50)

# Count how many times 20 appears
count_20 = numbers.count(20)
print("Count of 20:", count_20)

print("\nClasswork 4: Slicing and List Comprehensions")
# Classwork 4: Slicing and List Comprehensions
numbers = list(range(1, 11))  # Creates a list from 1 to 10
print("Original numbers list:", numbers)

# Create first_half
first_half = numbers[:5]
print("First half:", first_half)

# Create second_half
second_half = numbers[5:]
print("Second half:", second_half)

# List comprehension to create squares
squares = [x**2 for x in numbers]
print("Squares of numbers:", squares)

print("\nClasswork 5: List Manipulation and Aggregation")
# Classwork 5: List Manipulation and Aggregation
temperatures = [72, 68, 75, 70, 78, 74, 71]

# Calculate highest temperature
highest_temp = max(temperatures)
print("Highest temperature:", highest_temp)

# Calculate lowest temperature
lowest_temp = min(temperatures)
print("Lowest temperature:", lowest_temp)

# Calculate average temperature
average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)

# List comprehension to find temperatures above 70
above_70 = [temp for temp in temperatures if temp > 70]
print("Temperatures above 70:", above_70)
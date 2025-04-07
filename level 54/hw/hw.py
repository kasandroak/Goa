# 2. Use the map function to double the numbers in a list
numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", doubled_numbers)

# 3. Write a program using map to concatenate "Hello, " to each name in a list
names = ["Alice", "Bob", "Charlie"]
greeting_names = list(map(lambda name: "Hello, " + name, names))
print("Greeting Names:", greeting_names)

# 4. Use map to calculate the lengths of strings in a list
fruits = ["apple", "banana", "kiwi"]
fruit_lengths = list(map(lambda fruit: len(fruit), fruits))
print("Fruit Lengths:", fruit_lengths)

# 5. Use the filter function to keep only positive numbers from a list
numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive Numbers:", positive_numbers)

# 6. Write a program using filter to extract words starting with the letter "p" from a list
words = ["pear", "apple", "peach", "grape"]
words_starting_with_p = list(filter(lambda word: word[0] == 'p', words))
print("Words Starting with 'P':", words_starting_with_p)

# 7. Use filter to find numbers greater than 50 in a list
numbers = [10, 55, 42, 78, 65, 20]
numbers_greater_than_50 = list(filter(lambda x: x > 50, numbers))
print("Numbers Greater Than 50:", numbers_greater_than_50)

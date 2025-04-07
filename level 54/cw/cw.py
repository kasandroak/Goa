# MAPS
numbers = [1, 2, 3, 4, 5]
print("Squares:", list(map(lambda x: x ** 2, numbers)))

celsius = [0, 20, 30, 40]
print("Celsius to Fahrenheit:", list(map(lambda c: (c * 33.8) + 32, celsius)))

words = ["hello", "world", "python"]
print("Capitalized Words:", list(map(lambda word: word.capitalize(), words)))

# FILTERS
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Even Numbers:", list(filter(lambda x: x % 2 == 0, numbers)))

words = ["cat", "house", "tree", "car"]
print("Words with 4 or more characters:", list(filter(lambda word: len(word) >= 4, words)))

numbers = [3, 9, 15, 22, 27, 30]
print("Multiples of 3:", list(filter(lambda x: x % 3 == 0, numbers)))

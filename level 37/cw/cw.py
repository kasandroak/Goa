# Task 1: Format a String
name = input("Enter your name: ")
age = input("Enter your age: ")
formatted_sentence = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_sentence)

# Task 2: Join a List of Strings
words = ["Python", "is", "fun"]
joined_sentence = " ".join(words)
print(joined_sentence)

# Task 3: Split a String
sentence_to_split = input("Enter a sentence to split: ")
words_list = sentence_to_split.split()
print("List of words:", words_list)

# Task 4: Replace Substrings
sentence_to_replace = input("Enter a sentence to replace a word: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_sentence = sentence_to_replace.replace(old_word, new_word)
print("Modified sentence:", modified_sentence)

# Task 5: Convert to Lowercase
text_to_lower = input("Enter a string to convert to lowercase: ")
lowercase_text = text_to_lower.lower()
print("Lowercase version:", lowercase_text)

# Task 6: Convert to Uppercase
sentence_to_upper = input("Enter a sentence to convert to uppercase: ")
uppercase_sentence = sentence_to_upper.upper()
print("Uppercase version:", uppercase_sentence)

# Create a dictionary for the computer
computer = {
    "brand": "Dell",
    "model": "XPS 13",
    "processor": "Intel Core i7",
    "ram": "16GB",
    "storage": "512GB SSD"
}

# 2. Print all the keys of the dictionary
print("Keys of the dictionary:")
for key in computer:
    print(key)

# 3. Print all the values of the dictionary
print("\nValues of the dictionary:")
for value in computer.values():
    print(value)

# 4. Print both keys and values of the dictionary
print("\nKeys and values of the dictionary:")
for key, value in computer.items():
    print(f"{key}: {value}")

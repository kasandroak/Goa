# დავალება 1: შექმენით 3 dictionary
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"x": 10, "y": 20, "z": 30}
dict3 = {"apple": "fruit", "carrot": "vegetable", "chicken": "meat"}

# დავალება 2: გამოიტანეთ key-ები for loop და .items() მეთოდით
print("Dictionary 1 key-ები:")
for key, value in dict1.items():
    print(key)

print("\nDictionary 2 key-ები:")
for key, value in dict2.items():
    print(key)

print("\nDictionary 3 key-ები:")
for key, value in dict3.items():
    print(key)

# დავალება 3: გამოიტანეთ value-ები for loop და .items() მეთოდით
print("\nDictionary 1 value-ები:")
for key, value in dict1.items():
    print(value)

print("\nDictionary 2 value-ები:")
for key, value in dict2.items():
    print(value)

print("\nDictionary 3 value-ები:")
for key, value in dict3.items():
    print(value)

# დავალება 4: გამოიყენეთ list comprehension და შექმენით list 1-დან 1000-მდე
numbers = [i for i in range(1, 1001)]
print("\nList 1-დან 1000-მდე:", numbers[:10], "...")  # მხოლოდ პირველი 10 რიცხვი გამოიტანე

# დავალება 5: გამოიყენეთ list comprehension და შექმენით list 1-დან 100-მდე, გამრავლებული 2-ზე
even_numbers = [i * 2 for i in range(1, 101)]
print("\nList 1-დან 100-მდე, გამრავლებული 2-ზე:", even_numbers[:10], "...")  # მხოლოდ პირველი 10 რიცხვი გამოიტანე

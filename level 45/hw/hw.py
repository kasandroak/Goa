# დავალება 2: შექმენით dictionary 10 key:value pair'ით და გამოიტანეთ ყველა key .items() მეთოდის გამოყენებით
dict1 = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
    "f": 6, "g": 7, "h": 8, "i": 9, "j": 10
}

print("Dictionary 1 key-ები:")
for key, value in dict1.items():
    print(key)

# დავალება 3: შექმენით dictionary 10 key:value pair'ით და გამოიტანეთ ყველა value .items() მეთოდის გამოყენებით
dict2 = {
    "apple": "fruit", "carrot": "vegetable", "chicken": "meat", "dog": "animal", "elephant": "animal",
    "fish": "animal", "grape": "fruit", "honey": "food", "ice": "dessert", "juice": "drink"
}

print("\nDictionary 2 value-ები:")
for key, value in dict2.items():
    print(value)

# დავალება 4: list comprehension'ის მეშვეობით შექმენით list, რომელშიც იქნება 2'ზე გაყოფილი და 1'ით მეტი რიცხვები 50'დან 100'მდე
numbers_divided_and_plus_one = [(i / 2) + 1 for i in range(50, 101)]
print("\nList 50-დან 100-მდე, 2'ზე გაყოფილი და 1'ით მეტი:", numbers_divided_and_plus_one[:10], "...")  # მხოლოდ პირველი 10 რიცხვი

# დავალება 5: list comprehension'ის მეშვეობით შექმენით list, რომელშიც იქნება 2'ზე გამრავლებული და 1'ით მეტი რიცხვები 50'დან 100'მდე
numbers_multiplied_and_plus_one = [(i * 2) + 1 for i in range(50, 101)]
print("\nList 50-დან 100-მდე, 2'ზე გამრავლებული და 1'ით მეტი:", numbers_multiplied_and_plus_one[:10], "...")  # მხოლოდ პირველი 10 რიცხვი

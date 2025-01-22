# 1) რიცხვები 1-დან 100-მდე
numbers = [x for x in range(1, 101)]

# 2) რიცხვები 1-დან 100-მდე, 2-2-ის გამოტოვებით
numbers_odd = [x for x in range(1, 101, 2)]

# 3) სახელები, რომელთა შემადგენლობაში არ არის "a", და ყველა სახელის თავში "#" მოეწყობა
names = ["Alice", "Bob", "Charlie", "David"]
filtered_names = ["#" + name for name in names if "a" not in name.lower()]

# გამოვიტანოთ შედეგები
print("Numbers 1-100:", numbers)
print("Numbers 1-100 with step 2:", numbers_odd)
print("Filtered names:", filtered_names)

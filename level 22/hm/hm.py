# შექმენით საწყისი სიები
list1 = [1]
list2 = [2, 4]
list3 = [3, 6, 9]
list4 = [4, 8, 12, 16]
list5 = [5, 10, 15, 20, 25]
list6 = [6, 12, 18, 24, 30, 36]
list7 = [7, 14, 21, 28, 35, 42, 49]
list8 = [8, 16, 24, 32, 40, 48, 56, 64]
list9 = [9, 18, 27, 36, 45, 54, 63, 72, 81]
list10 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# გამოიტანეთ საწყისი სიები
print("Initial lists:")
for i in range(1, 11):
    current_list = globals()[f'list{i}']
    print(f"list{i}: {current_list}")

# შეცვალეთ ყველა ელემენტი სიაში
for i in range(1, 11):
    current_list = globals()[f'list{i}']
    new_values = [x * 2 for x in current_list]  # ელემენტების გაორმაგება
    globals()[f'list{i}'] = new_values

# გამოიტანეთ საბოლოო სიები
print("\nUpdated lists:")
for i in range(1, 11):
    current_list = globals()[f'list{i}']
    print(f"list{i}: {current_list}")
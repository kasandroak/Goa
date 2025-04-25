# 1) მხოლოდ ისეთი რიცხვები რომლებიც >= 40
numbers1 = [10, 25, 40, 55, 70, 33, 42]
filtered_numbers = list(filter(lambda x: x >= 40, numbers1))
print("რიცხვები რომლებიც მეტია ან ტოლია 40-ის:", filtered_numbers)

# 2) ყველა რიცხვის კვადრატი
numbers2 = [2, 5, 7, 9, 12]
squared_numbers = list(map(lambda x: x ** 2, numbers2))
print("რიცხვების კვადრატები:", squared_numbers)

# 3) მხოლოდ ისეთი სტრინგები რომლებიც მთავრდება 'a' სიმბოლოთი
words = ["banana", "apple", "mango", "papaya", "kiwi", "avocado", "coca"]
words_ending_with_a = list(filter(lambda word: word.endswith('a'), words))
print("სიტყვები რომლებიც მთავრდება 'a'-ზე:", words_ending_with_a)

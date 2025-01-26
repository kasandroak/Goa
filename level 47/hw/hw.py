# 1. სიტყვის რიცხვი ტექსტში
def count_words(text):
    words = text.split()
    return len(words)

# 2. პირობითი ოპერაცია რიცხვის დადებითობის შემოწმებისთვის
def check_number(num):
    if num > 0:
        return "რიცხვი არის დადებითი"
    elif num < 0:
        return "რიცხვი არის უარყოფითი"
    else:
        return "რიცხვი არის ნული"

# 3. მომხმარებლის ასაკის კატეგორიზაცია
def categorize_age(age):
    if age < 13:
        return "ბავშვი"
    elif 13 <= age < 20:
        return "თინეიჯერი"
    elif 20 <= age < 60:
        return "ზრდასრული"
    else:
        return "მოხუცი"

# 4. ლუწი და კენტი რიცხვთა სიის პოვნა
def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

# 5. საშუალო რიცხვის პოვნა
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# გამოსაყენებელი მაგალითები:

# 1. სიტყვის რიცხვი
text = "ეს არის მაგალითი ტექსტი"
print(f"სიტყვის რიცხვი: {count_words(text)}")  # Output: 4

# 2. რიცხვის დადებითობის შემოწმება
num = int(input("შეიყვანეთ რიცხვი: "))
print(check_number(num))  # დადებითი, უარყოფითი ან ნულოვანი

# 3. ასაკის კატეგორიზაცია
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
print(categorize_age(age))  # ასაკობრივი კატეგორია

# 4. ლუწი და კენტი რიცხვების პოვნა
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = separate_even_odd(numbers)
print("ლუწი რიცხვები:", even)
print("კენტი რიცხვები:", odd)

# 5. საშუალო რიცხვის პოვნა
print("საშუალო რიცხვი:", average(numbers))

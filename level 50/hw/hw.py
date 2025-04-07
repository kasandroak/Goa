# 1. NameError - შეცდომა, როდესაც ცვლადი არ არის განსაზღვრული
# 2. IndexError - შეცდომა, როდესაც ინდექსი არ არსებობს სიაში
# 3. ValueError - შეცდომა, როდესაც ცვლადის მნიშვნელობა არ არის სწორი

try:
    # 1. NameError: ცვლადი 'x' არ არის განსაზღვრული
    print(x)  # აქ შეიქმნება NameError, რადგან x არ არის განსაზღვრული
    
    # 2. IndexError: სია არ აქვს იმდენი ელემენტი
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError - აქ ვცდილობთ დავაკონკრეტოთ ინდექსი, რომელიც არ არსებობს
    
    # 3. ValueError: ვცდილობთ აღვიქვათ არასწორი ტიპის მონაცემები
    number = int("hello")  # ValueError - ეს არ არის რიცხვი, ამიტომ გაუმართლა შეცდომა

except NameError as ne:
    # დაჭერა NameError შეცდომის დროს
    print(f"NameError: {ne}")  # ნაჩვენები იქნება, რომ ცვლადი არ არის განსაზღვრული

except IndexError as ie:
    # დაჭერა IndexError შეცდომის დროს
    print(f"IndexError: {ie}")  # ნაჩვენები იქნება, რომ ინდექსი არ არსებობს სიაში

except ValueError as ve:
    # დაჭერა ValueError შეცდომის დროს
    print(f"ValueError: {ve}")  # ნაჩვენები იქნება, რომ მონაცემების კონვერტაცია ვერ მოხდება

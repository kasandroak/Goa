def categorize_age(age):
    if age < 13:
        return "ბავშვი"
    elif 13 <= age < 20:
        return "თინეიჯერი"
    elif 20 <= age < 60:
        return "ზრდასრული"
    else:
        return "მოხუცი"

# მომხმარებლის ასაკი
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
print(categorize_age(age))  # ასაკობრივი კატეგორია

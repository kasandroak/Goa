# price და discount ცვლადების შექმნა
price = float(input("შეიტანეთ პროდუქტის ფასი: "))
discount = float(input("შეიტანეთ ფასდაკლების პროცენტი: "))

# საბოლოო ფასის გამოთვლა
final_price = price - (price * discount / 100)

# შედეგის ეკრანზე გამოქვეყნება
print(f"ფასდაკლების შემდეგ საბოლოო ფასი არის: {final_price:.2f}")

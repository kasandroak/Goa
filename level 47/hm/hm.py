# 1) ასაკის შეკითხვა და საიტერაციო ცვლადის ჩვენება
age = int(input("რამდენი წლის ხართ? "))
for i in range(age):
    print(i + 1)

# 2) ტემპერატურის გადაყვანა ფარენჰეიტში
celsius = float(input("შეიტანეთ ტემპერატურა ცელსიუსებში: "))
fahrenheit = (celsius * 9/5) + 32
print(f"ფარენჰეიტში: {fahrenheit}")

# 3) შედარების და ლოგიკური ოპერატორების მაგალითები
print("შედარების მაგალითები:")
print("5 == 5:", 5 == 5)  # True
print("5 != 3:", 5 != 3)  # True
print("3 < 5:", 3 < 5)    # True

print("ლოგიკური მაგალითები:")
print("True and False:", True and False)  # False
print("True or False:", True or False)      # True
print("not True:", not True)                 # False

# 4) სამკუთხედის დახატვა
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

# 5) 20 წლის ასაკის ლოგიკური ოპერატორი
is_twenty = (age == 20)
print("20 წლის ხართ:", is_twenty)

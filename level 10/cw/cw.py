# სამი ცვლადის შექმნა და მათი მნიშვნელობების შემოტანა მომხმარებლისგან
num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
num3 = float(input("შეიტანეთ მესამე რიცხვი: "))

# ოპერაციები ამ რიცხვებზე
print("გამოაკელით (num1 - num2):", num1 - num2)
print("გამრავლება (num1 * num2):", num1 * num2)
print("გაყოფა (num1 / num2):", num1 / num2 if num2 != 0 else "ზეროს მიერ გაყოფა შეუძლებელია")
print("ჯამი (num1 + num2):", num1 + num2)
print("გამოაკელით (num1 - num3):", num1 - num3)
print("გამრავლება (num1 * num3):", num1 * num3)
print("გაყოფა (num1 / num3):", num1 / num3 if num3 != 0 else "ზეროს მიერ გაყოფა შეუძლებელია")
print("ჯამი (num1 + num3):", num1 + num3)
print("გამოაკელით (num2 - num3):", num2 - num3)
print("გამრავლება (num2 * num3):", num2 * num3)
print("გაყოფა (num2 / num3):", num2 / num3 if num3 != 0 else "ზეროს მიერ გაყოფა შეუძლებელია")
print("ჯამი (num2 + num3):", num2 + num3)

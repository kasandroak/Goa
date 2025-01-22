# 10 მთელი რიცხვების სია, 1-დან 10-მდე
numbers = list(range(1, 11))
print("სრული სია:", numbers)

# პირველი 5 ელემენტი
first_five = numbers[:5]
print("პირველი 5 ელემენტი:", first_five)

# ბოლო 3 ელემენტი
last_three = numbers[-3:]
print("ბოლო 3 ელემენტი:", last_three)

# ყოველი მეორე ელემენტი
every_second = numbers[::2]
print("ყოველი მეორე ელემენტი:", every_second)

# დავალება 3
# 6 სტრიქონის სია ხილის
fruits = ['ვაშლი', 'ბანანი', 'ალუბალი', 'თარიღი', 'ლეღვი', 'ყურძენი']
print("სრული სია ხილებით:", fruits)

# შებრუნებული სია
reversed_fruits = fruits[::-1]
print("შებრუნებული სია:", reversed_fruits)

# შუა ორი ხილის შეცვლა
fruits[2:4] = ['კივი', 'ცაცხვი']
print("განახლებული სია:", fruits)
# 1) ფუნქცია გაორმაგებისთვის
def double_number(n):
    return n * 2

# 2) ფუნქცია მისალმებისთვის
def greet(name):
    return f"Hello, {name}!"

# 3) ფუნქცია ლუწი რიცხვის შემოწმებისთვის
def is_even(num):
    return num % 2 == 0

# 4) მარტივი ფუნქცია default value-სთვის
def greet_person(name="Guest"):
    return f"Welcome, {name}!"

# 5) ფუნქცია სახელის სიდიდით
def nickname(name):
    return name[:3]

# ტესტირება:
print(double_number(5))        # 10
print(greet("Alice"))          # "Hello, Alice!"
print(is_even(4))              # True
print(greet_person())          # "Welcome, Guest!"
print(nickname("Jonathan"))    # "Jon"

def double_integer(n):
    return n * 2

def greet(name):
    return f"გამარჯობა, {name}!"

def is_even(num):
    return num % 2 == 0

def greet_user(name="მსოფლიო"):
    return f"გამარჯობა, {name}!"

def nickname(name):
    return name[:3]

# მაგალითები ფუნქციების გამოყენებისთვის
print(double_integer(5))  # 10
print(greet("ნიკა"))     # "გამარჯობა, ნიკა!"
print(is_even(4))        # True
print(is_even(3))        # False
print(greet_user())      # "გამარჯობა, მსოფლიო!"
print(greet_user("ანა")) # "გამარჯობა, ანა!"
print(nickname("გიორგი")) # "გიე"
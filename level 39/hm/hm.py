# 1. ფუნცქცია, რომელიც არგუმენტად იღებს ინტეჯერს და დაბრუნებს გაორმაგებულ მნიშვნელობას
def double_integer(n):
    return n * 2

# 2. ფუნქცია, რომელიც იღებს ადამიანის სახელს და აბრუნებს მისალმების ტექსტს
def greet(name):
    return f"გამარჯობა, {name}!"

# 3. ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი
def is_even(num):
    return num % 2 == 0

# 4. მარტივი ფუნქცია, რომელიც აქვს default value
def repeat_string(string, times=1):
    return string * times

# 5. ფუნქცია, რომელიც არგუმენტად იღებს სახელს და აბრუნებს პირველი სამი ასო
def nickname(name):
    return name[:3]

# გამოყენების მაგალითები
print(double_integer(5))         # 10
print(greet("გიორგი"))          # "გამარჯობა, გიორგი!"
print(is_even(4))                # True
print(is_even(3))                # False
print(repeat_string("hello", 3)) # "hellohellohello"
print(nickname("ალექსანდრე"))   # "ალე"
